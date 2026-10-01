# 开源寻宝 · OSS Treasure Hunt

每天抽一张寻宝卡，带着一个有趣的小目标逛 GitHub 和 Gitee。

```text
开源寻宝 · 2026-10-01
今日任务：找一个把数学变成图像的作品。
搜索词：generative art
GitHub: https://github.com/search?q=generative%20art&type=repositories
Gitee: https://so.gitee.com/?q=generative%20art
```

## 使用

需要 Python 3.9 或更新版本，无第三方依赖。

```bash
python oss_treasure_hunt.py
python oss_treasure_hunt.py --site github --open
python oss_treasure_hunt.py --site gitee --seed rust
```

默认每天得到同一张卡，方便稍后接着探索。传入 `--seed` 可固定为另一张卡；传入 `--open` 才会在浏览器中打开链接。程序本身不会发起网络请求或保存数据；使用 `--open` 时，浏览器会把搜索词发送给对应平台。

## 添加寻宝卡

在 `MISSIONS` 中添加一组“任务描述”和“搜索词”即可。

## License

MIT
