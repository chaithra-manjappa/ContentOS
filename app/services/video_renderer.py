"""Video Renderer."""

from pathlib import Path

import ffmpeg

from app.models.video_project import VideoProject


class VideoRenderer:
    """
    Creates an MP4 from generated scene images and narration audio.
    """

    def render(
        self,
        project: VideoProject,
        output_path: Path,
    ) -> VideoProject:

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        temp_directory = output_path.parent

        # -------------------------------------------------
        # IMAGE CONCAT FILE
        # -------------------------------------------------

        image_concat = temp_directory / "images.txt"

        with image_concat.open(
            "w",
            encoding="utf-8",
        ) as file:

            for scene in project.scenes:

                if scene.image_path is None:
                    continue

                file.write(
                    f"file '{scene.image_path.resolve()}'\n"
                )

                file.write(
                    f"duration {scene.duration}\n"
                )

            if project.scenes:

                last = project.scenes[-1]

                if last.image_path is not None:

                    file.write(
                        f"file '{last.image_path.resolve()}'\n"
                    )

        # -------------------------------------------------
        # AUDIO CONCAT FILE
        # -------------------------------------------------

        audio_concat = temp_directory / "audio.txt"

        with audio_concat.open(
            "w",
            encoding="utf-8",
        ) as file:

            for scene in project.scenes:

                if scene.audio_path is None:
                    continue

                file.write(
                    f"file '{scene.audio_path.resolve()}'\n"
                )

        narration_path = temp_directory / "narration.wav"

        (
            ffmpeg
            .input(
                str(audio_concat),
                format="concat",
                safe=0,
            )
            .output(
                str(narration_path),
                acodec="pcm_s16le",
            )
            .overwrite_output()
            .run(
                quiet=False,
            )
        )

        # -------------------------------------------------
        # VIDEO INPUT
        # -------------------------------------------------

        video = ffmpeg.input(
            str(image_concat),
            format="concat",
            safe=0,
        )

        # -------------------------------------------------
        # AUDIO INPUT
        # -------------------------------------------------

        audio = ffmpeg.input(
            str(narration_path),
        )

        # -------------------------------------------------
        # MERGE VIDEO + AUDIO
        # -------------------------------------------------

        (
            ffmpeg
            .output(
                video.video,
                audio.audio,
                str(output_path),
                vcodec="libx264",
                acodec="aac",
                pix_fmt="yuv420p",
                shortest=None,
                movflags="+faststart",
            )
            .overwrite_output()
            .global_args("-loglevel", "error")
            .run(
                quiet=False,
            )
        )

        project.video_path = output_path

        return project