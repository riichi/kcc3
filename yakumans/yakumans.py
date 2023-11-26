from dataclasses import dataclass
from enum import Enum


class YakumanType(Enum):
    REGULAR = 1
    INITIAL = 2
    OPTIONAL = 3


@dataclass
class Yakuman:
    id: str
    name: str
    japanese_name: str
    type: YakumanType
    double: bool

    @property
    def verbose_name(self):
        return f"{self.name} ({self.japanese_name})"

    def __str__(self):
        return self.name


KAZOE_YAKUMAN = Yakuman(
    id="KAZOE_YAKUMAN",
    name="Kazoe Yakuman",
    japanese_name="数え役満",
    type=YakumanType.REGULAR,
    double=False,
)
KOKUSHI_MUSOU = Yakuman(
    id="KOKUSHI_MUSOU",
    name="Kokushi musou",
    japanese_name="国士無双",
    type=YakumanType.REGULAR,
    double=False,
)
KOKUSHI_MUSOU_JUUSAN_MENMACHI = Yakuman(
    id="KOKUSHI_MUSOU_JUUSAN_MENMACHI",
    name="Kokushi musou juusan menmachi",
    japanese_name="国士無双１３面待ち",
    type=YakumanType.REGULAR,
    double=True,
)
SUUANKOU = Yakuman(
    id="SUUANKOU",
    name="Suuankou",
    japanese_name="四暗刻",
    type=YakumanType.REGULAR,
    double=False,
)
SUUANKOU_TANKI = Yakuman(
    id="SUUANKOU_TANKI",
    name="Suuankou tanki",
    japanese_name="四暗刻単騎",
    type=YakumanType.REGULAR,
    double=True,
)
DAISANGEN = Yakuman(
    id="DAISANGEN",
    name="Daisangen",
    japanese_name="大三元",
    type=YakumanType.REGULAR,
    double=False,
)
SHOUSUUSHII = Yakuman(
    id="SHOUSUUSHII",
    name="Shousuushii",
    japanese_name="小四喜",
    type=YakumanType.REGULAR,
    double=False,
)
DAISUUSHII = Yakuman(
    id="DAISUUSHII",
    name="Daisuushii",
    japanese_name="大四喜",
    type=YakumanType.REGULAR,
    double=True,
)
TSUUIISOU = Yakuman(
    id="TSUUIISOU",
    name="Tsuuiisou",
    japanese_name="字一色",
    type=YakumanType.REGULAR,
    double=False,
)
CHINROUTOU = Yakuman(
    id="CHINROUTOU",
    name="Chinroutou",
    japanese_name="清老頭",
    type=YakumanType.REGULAR,
    double=False,
)
RYUUIISOU = Yakuman(
    id="RYUUIISOU",
    name="Ryuuiisou",
    japanese_name="緑一色",
    type=YakumanType.REGULAR,
    double=False,
)
CHUUREN_POUTOU = Yakuman(
    id="CHUUREN_POUTOU",
    name="Chuuren poutou",
    japanese_name="九連宝燈",
    type=YakumanType.REGULAR,
    double=False,
)
JUNSEI_CHUUREN_POUTOU = Yakuman(
    id="JUNSEI_CHUUREN_POUTOU",
    name="Junsei chuuren poutou",
    japanese_name="純正九蓮宝燈",
    type=YakumanType.REGULAR,
    double=True,
)
SUUKANTSU = Yakuman(
    id="SUUKANTSU",
    name="Suukantsu",
    japanese_name="四槓子",
    type=YakumanType.REGULAR,
    double=False,
)

TENHOU = Yakuman(
    id="TENHOU",
    name="Tenhou",
    japanese_name="天和",
    type=YakumanType.INITIAL,
    double=False,
)
CHIIHOU = Yakuman(
    id="CHIIHOU",
    name="Chiihou",
    japanese_name="地和",
    type=YakumanType.INITIAL,
    double=False,
)

DAICHISEI = Yakuman(
    id="DAICHISEI",
    name="Daichisei",
    japanese_name="大七星",
    type=YakumanType.OPTIONAL,
    double=True,
)
DAISHARIN = Yakuman(
    id="DAISHARIN",
    name="Daisharin",
    japanese_name="大車輪",
    type=YakumanType.OPTIONAL,
    double=False,
)
DAICHIKURIN = Yakuman(
    id="DAICHIKURIN",
    name="Daichikurin",
    japanese_name="大竹林",
    type=YakumanType.OPTIONAL,
    double=False,
)
DAISUURIN = Yakuman(
    id="DAISUURIN",
    name="Daisuurin",
    japanese_name="大数林",
    type=YakumanType.OPTIONAL,
    double=False,
)
IISHOKU_YONJUN = Yakuman(
    id="IISHOKU_YONJUN",
    name="Iishoku yonjun",
    japanese_name="一色四順",
    type=YakumanType.OPTIONAL,
    double=False,
)
OPEN_RIICHI = Yakuman(
    id="OPEN_RIICHI",
    name="Open riichi",
    japanese_name="オープン立直",
    type=YakumanType.OPTIONAL,
    double=False,
)
PAARENCHAN = Yakuman(
    id="PAARENCHAN",
    name="Paarenchan",
    japanese_name="八連荘",
    type=YakumanType.OPTIONAL,
    double=False,
)
RENHOU = Yakuman(
    id="RENHOU",
    name="Renhou",
    japanese_name="人和",
    type=YakumanType.OPTIONAL,
    double=False,
)
SUURENKOU = Yakuman(
    id="SUURENKOU",
    name="Suurenkou",
    japanese_name="四連刻",
    type=YakumanType.OPTIONAL,
    double=False,
)
SHIISANPUUTAA = Yakuman(
    id="SHIISANPUUTAA",
    name="Shiisanpuutaa",
    japanese_name="十三不塔",
    type=YakumanType.OPTIONAL,
    double=False,
)
SHIISUUPUUTAA = Yakuman(
    id="SHIISUUPUUTAA",
    name="Shiisuupuutaa",
    japanese_name="十四不塔",
    type=YakumanType.OPTIONAL,
    double=False,
)

YAKUMANS = (
    KAZOE_YAKUMAN,
    KOKUSHI_MUSOU,
    KOKUSHI_MUSOU_JUUSAN_MENMACHI,
    SUUANKOU,
    SUUANKOU_TANKI,
    DAISANGEN,
    SHOUSUUSHII,
    DAISUUSHII,
    TSUUIISOU,
    CHINROUTOU,
    RYUUIISOU,
    CHUUREN_POUTOU,
    JUNSEI_CHUUREN_POUTOU,
    SUUKANTSU,
    TENHOU,
    CHIIHOU,
    DAICHISEI,
    DAISHARIN,
    DAICHIKURIN,
    DAISUURIN,
    IISHOKU_YONJUN,
    OPEN_RIICHI,
    PAARENCHAN,
    RENHOU,
    SUURENKOU,
    SHIISANPUUTAA,
    SHIISUUPUUTAA,
)
YAKUMANS_BY_NAME = sorted(YAKUMANS, key=lambda x: x.name)


def yakuman_by_id(yaku_id: str) -> Yakuman:
    return next(x for x in YAKUMANS if x.id == yaku_id)


def yakuman_by_name(name: str) -> Yakuman:
    return next(x for x in YAKUMANS if x.name == name)
