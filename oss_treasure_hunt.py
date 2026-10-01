#!/usr/bin/env python3
"""Pick a daily open-source discovery mission for GitHub and Gitee."""

import argparse
from datetime import date
import random
import sys
from urllib.parse import quote
import webbrowser

MISSIONS = (
    ("找到一个把数学变成图像的作品。", "generative art"),
    ("找一个小到能读完核心实现的迷你语言。", "tiny programming language"),
    ("找一款让终端变成游乐场的小游戏。", "terminal game"),
    ("找一个断网时也能继续使用的工具。", "offline first"),
    ("找一个会自己长出旋律的项目。", "procedural music"),
    ("找一个可以亲手画出小世界的编辑器。", "pixel art editor"),
    ("找一个把代码当画笔的创意作品。", "creative coding"),
    ("找一个能让旧设备派上新用场的项目。", "home automation"),
    ("找一个只用文字就撑起整个世界的游戏。", "text adventure game"),
    ("找一个能用参数生成图形的工具。", "svg generator"),
    ("找一个把网络服务缩到极小的实现。", "tiny web server"),
    ("找一个能模拟真实或幻想世界的项目。", "open source simulation"),
)


def search_url(site, query):
    term = quote(query, safe="")
    if site == "GitHub":
        return f"https://github.com/search?q={term}&type=repositories"
    return f"https://so.gitee.com/?q={term}"


def main():
    parser = argparse.ArgumentParser(description="抽一张开源项目寻宝卡，并生成 GitHub/Gitee 搜索链接。")
    parser.add_argument("--site", choices=("both", "github", "gitee"), default="both", help="搜索平台（默认：both）")
    parser.add_argument("--seed", help="固定抽卡结果，方便重现；默认每天固定一张")
    parser.add_argument("--open", action="store_true", dest="open_browser", help="在浏览器中打开搜索链接")
    args = parser.parse_args()

    today = date.today().isoformat()
    mission, query = random.Random(args.seed or today).choice(MISSIONS)
    print(f"开源寻宝 · {today}")
    print(f"今日任务：{mission}")
    print(f"搜索词：{query}")

    sites = {"github": ("GitHub",), "gitee": ("Gitee",), "both": ("GitHub", "Gitee")}[args.site]
    for site in sites:
        url = search_url(site, query)
        print(f"{site}: {url}")
        if args.open_browser:
            try:
                opened = webbrowser.open_new_tab(url)
            except webbrowser.Error as error:
                print(f"无法打开浏览器，请复制链接访问：{error}", file=sys.stderr)
                continue
            if not opened:
                print("浏览器没有打开页面；请复制上方链接访问。", file=sys.stderr)


if __name__ == "__main__":
    main()
