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
from camel.agents import ChatAgent
from camel.messages import AssistantSystemMessage, UserChatMessage
from camel.prompts import SingleShotPromptTemplateDict
from camel.typing import TaskType, RoleType


def main(key: str = "generate_users", num_roles: int = 50):

    single_shot_template = SingleShotPromptTemplateDict()
    assistant_sys_msg_prompt = single_shot_template[RoleType.ASSISTANT]

    assistant_sys_msg = AssistantSystemMessage(
        role_name="Assistant",
        content=assistant_sys_msg_prompt,
    )
    agent = ChatAgent(assistant_sys_msg)
    agent.reset()

    user_msg = UserChatMessage(
        role_name="User",
        content="Name 10 animals.",
    )
    assistant_response = agent.step(user_msg)
    if assistant_response.msgs is not None:
        print(assistant_response.msg.content)


if __name__ == "__main__":
    main("generate_users", 50)
    main("generate_assistants", 50)
