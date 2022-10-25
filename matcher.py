from typing import Mapping

COMMON_NAMES = """James,John,Robert,Michael,William,
David,Richard,Charles,Joseph,Thomas,Christopher,
Daniel,Paul,Mark,Donald,George,Kenneth,Steven,
Edward,Brian,Ronald,Anthony,Kevin,Jason,Matthew,
Gary,Timothy,Jose,Larry,Jeffrey,Frank,Scott,
Eric,Stephen,Andrew,Raymond,Gregory,Joshua,Jerry,
Dennis,Walter,Patrick,Peter,Harold,Douglas,
Henry,Carl,Arthur,Ryan,Roger""".replace("\n", "").split(",")


def match(data: str) -> Mapping[str, int]:
    matches = dict()
    for w in COMMON_NAMES:
        i = data.find(w)
        if i >= 0:
            matches[w] = i
    return matches
