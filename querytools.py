import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(
        command="python",
        args=["../weather/weather.py"],
        env=None,
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()       # MCP 必備的握手
            tools = (await session.list_tools()).tools
            print("可用工具：", [t.name for t in tools])

if __name__ == "__main__":
    asyncio.run(main())
