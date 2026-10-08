#!/usr/bin/env python3
"""网名生成器 - 随机生成各种风格的网名"""

import random
import sys

STYLES = {
    "古风": {
        "prefixes": ["墨", "云", "雪", "风", "月", "竹", "梅", "兰", "霜", "烟", "雨", "花", "柳", "松", "鹤"],
        "suffixes": ["落", "归", "隐", "吟", "眠", "醉", "舞", "笑", "行", "歌", "梦", "影", "寒", "染", "渡"],
        "patterns": [
            "{p}中{s}", "{p}{s}人", "一{p}{s}", "{p}里{s}", "半{p}半{s}",
            "{p}{p2}{s}", "听{p}{s}", "{p}下{s}", "独{s}{p}", "无{p}不{s}",
        ],
    },
    "可爱": {
        "prefixes": ["小", "奶", "甜", "软", "萌", "糖", "棉", "泡", "果", "蜜"],
        "suffixes": ["兔", "猫", "熊", "鹿", "团", "包", "糖", "酱", "丸", "桃"],
        "patterns": [
            "{p}{s}", "{p}{p2}{s}", "一只{p}{s}", "{p}{s}子", "爱吃{s}的{p}{s2}",
            "{s}{s2}不是{s}", "今天也是{p}{s}", "{p}味{s}", "超级{p}{s}", "{p}{s}呀",
        ],
    },
    "中二": {
        "prefixes": ["暗", "黑", "血", "影", "焰", "魔", "灵", "幻", "冥", "绝"],
        "suffixes": ["刃", "魂", "翼", "瞳", "夜", "狼", "龙", "帝", "神", "王"],
        "patterns": [
            "{p}{s}之主", "被封印的{p}{s}", "{p}之{s}", "最后的{p}{s}", "第七{p}{s}",
            "{p}{s}觉醒", "失落的{p}{s}", "{p}{p2}{s}", "永恒{p}{s}", "无尽{p}{s}",
        ],
    },
    "搞笑": {
        "prefixes": ["快乐", "迷路", "躺平", "佛系", "社恐", "摸鱼", "干饭", "摆烂", "咸鱼", "划水"],
        "suffixes": ["大师", "选手", "冠军", "专家", "达人", "小能手", "代言人", "继承者", "本人", "课代表"],
        "patterns": [
            "{p}{s}", "职业{p}{s}", "{p}界{s}", "全网最{p}的人", "不{p}就难受",
            "一天不{p}浑身难受", "{p}第一名", "退役{p}{s}", "{p}但没完全{p}", "被迫营业的{p}{s}",
        ],
    },
    "文艺": {
        "prefixes": ["晚", "夏", "秋", "春", "海", "星", "光", "木", "岛", "林"],
        "suffixes": ["风", "雨", "信", "歌", "诗", "屿", "鲸", "鸟", "河", "野"],
        "patterns": [
            "{p}天的{s}", "给{s}的{p}安", "{p}日{s}语", "与{s}书", "{p}{s}不惊",
            "第三封{s}", "{p}末{s}至", "像{p}天的{s}", "那年{p}{s}", "{p}色{s}声",
        ],
    },
}


def generate(style_name, count=5):
    style = STYLES[style_name]
    results = set()
    while len(results) < count:
        pattern = random.choice(style["patterns"])
        p = random.choice(style["prefixes"])
        p2 = random.choice(style["prefixes"])
        s = random.choice(style["suffixes"])
        s2 = random.choice(style["suffixes"])
        name = pattern.format(p=p, p2=p2, s=s, s2=s2)
        results.add(name)
    return list(results)


def main():
    style_names = list(STYLES.keys())

    if len(sys.argv) > 1:
        chosen = sys.argv[1]
        if chosen not in STYLES:
            print(f"未知风格: {chosen}")
            print(f"可用风格: {', '.join(style_names)}")
            sys.exit(1)
        styles_to_show = [chosen]
    else:
        styles_to_show = style_names

    count = 5
    if len(sys.argv) > 2:
        count = int(sys.argv[2])

    for style_name in styles_to_show:
        print(f"\n{'='*30}")
        print(f"  【{style_name}】风格")
        print(f"{'='*30}")
        names = generate(style_name, count)
        for i, name in enumerate(names, 1):
            print(f"  {i}. {name}")

    print(f"\n用法: python nickname_generator.py [风格] [数量]")
    print(f"可用风格: {', '.join(style_names)}")


if __name__ == "__main__":
    main()
