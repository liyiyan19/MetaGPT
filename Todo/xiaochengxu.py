import asyncio
import time

from metagpt.environment.mgx.mgx_env import MGXEnv
from metagpt.roles.di.engineer2 import Engineer2
from metagpt.roles.di.team_leader import TeamLeader
from metagpt.schema import Message


async def main(requirement="", user_defined_recipient="", enable_human_input=False, allow_idle_time=30):
    env = MGXEnv()
    env.add_roles([TeamLeader(), Engineer2()])

    msg = Message(content=requirement)
    env.attach_images(msg)  # attach image content if applicable

    if user_defined_recipient:
        msg.send_to = {user_defined_recipient}
        env.publish_message(msg, user_defined_recipient=user_defined_recipient)
    else:
        env.publish_message(msg)

    allow_idle_time = allow_idle_time if enable_human_input else 1
    start_time = time.time()
    while time.time() - start_time < allow_idle_time:
        if not env.is_idle:
            await env.run()
            start_time = time.time()  # reset start time


if __name__ == "__main__":
    idea = """
    开发IPIP人格测评小程序，要求：
    1. 支持50/300题动态切换模式
    2. 生成大五人格雷达图
    3. 集成微信/抖音双平台分享功能
    技术约束：
    - 前端必须使用UniApp+Vue3+Vant4
    - 后端必须使用SpringBoot3.0
    - 数据库采用MySQL
    - 数据可视化采用ECharts
    - 包含自动化测试套件
    """
    user_defined_recipient = ""

    asyncio.run(
        main(
            requirement=idea,
            user_defined_recipient=user_defined_recipient,
            enable_human_input=False,
            allow_idle_time=60,
        )
    )


if __name__ == "__main__":
    # 整合需求描述

    
    asyncio.run(startup(idea=idea))