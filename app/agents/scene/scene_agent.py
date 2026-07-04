"""Scene Agent."""

from app.clients.base_llm import BaseLLM
from app.models.scene import Scene
from app.models.video_project import VideoProject
from app.utils.json_parser import JSONParser


class SceneAgent:
    """
    Converts a reel script into a VideoProject.
    """

    def __init__(
        self,
        llm: BaseLLM,
    ) -> None:

        self._llm = llm

    def generate(
        self,
        script: str,
    ) -> VideoProject:

        prompt = f"""
You are an expert Instagram Reel creator.

Convert the following script into a storyboard.

Return ONLY valid JSON.

The JSON MUST follow this schema exactly.

{{
    "title": "Video Title",
    "scenes": [
        {{
            "number": 1,
            "duration": 5,
            "visual_prompt": "Describe what should appear on screen.",
            "narration": "Voice over text.",
            "caption": "Caption shown on screen."
        }}
    ]
}}

Rules:

- Return ONLY JSON.
- No markdown.
- No explanation.
- No ```json.
- Each scene should be between 4 and 6 seconds.
- Create between 5 and 8 scenes.

Script:

{script}
"""

        response = self._llm.generate(prompt)

        data = JSONParser.parse(response)

        project = VideoProject(
            title=data["title"],
        )

        for scene_data in data["scenes"]:

            scene = Scene(
                number=scene_data["number"],
                duration=scene_data["duration"],
                visual_prompt=scene_data["visual_prompt"],
                narration=scene_data["narration"],
                caption=scene_data["caption"],
            )

            project.scenes.append(scene)

        return project