"""Video Renderer."""

from pathlib import Path

import ffmpeg

from app.models.video_project import VideoProject


class VideoRenderer:
    """
    Renders a VideoProject into an MP4 file.
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

        input_files: list[tuple[Path, int]] = []

        for scene in project.scenes:

            if scene.image_path is None:
                continue

            input_files.append(
                (
                    scene.image_path,
                    scene.duration,
                )
            )

        if not input_files:
            raise RuntimeError(
                "No scene images were found to render."
            )

        concat_file = output_path.parent / "images.txt"

        with concat_file.open(
            "w",
            encoding="utf-8",
        ) as file:

            for image_path, duration in input_files:

                file.write(
                    f"file '{image_path.resolve()}'\n"
                )

                file.write(
                    f"duration {duration}\n"
                )

            # FFmpeg requires the final image to be repeated.
            file.write(
                f"file '{input_files[-1][0].resolve()}'\n"
            )

        (
            ffmpeg
            .input(
                str(concat_file),
                format="concat",
                safe=0,
            )
            .output(
                str(output_path),
                pix_fmt="yuv420p",
                vcodec="libx264",
            )
            .overwrite_output()
            .run(
                 overwrite_output=True,
            )
        )

        project.video_path = output_path

        return project