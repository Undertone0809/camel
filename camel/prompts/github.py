# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
from typing import Any

from camel.prompts.base import TextPrompt, TextPromptDict


class GitHubPromptTemplateDict(TextPromptDict):
    r"""A dictionary containing :obj:`TextPrompt` used in the `GitHub`
    task.

    Attributes:
        SOLVE_ISSUE (TextPrompt): A prompt to solve an issue
            in code based on the original source code and the
            issue description.
    """

    SOLVE_ISSUE = TextPrompt(
        """You need to solve the issue with number: {issue_number}
For this you will have to use the provided github function to retrieve
that issue. You will get all the necessary parameters to later create a
pull request.

When you have the issue, please follow the instruction and make the necessary
changes to the source code provided. Once you have made the changes, you will
need to use another provided github function to create a pull request
that updates the file on the provided file path in the repository {repo_name}.
The new_content property of the function should be the corrected source code.
Return response of this function as the output of this task.
"""
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.update(
            {
                "solve_issue": self.SOLVE_ISSUE,
            }
        )