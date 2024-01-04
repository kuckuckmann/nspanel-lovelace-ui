from libs.helper import iid, rgb_dec565
from libs.icon_mapping import get_icon_char
from libs.localization import get_translation


class Card:
    def __init__(self, locale, config, panel=None):
        self.iid = iid()
        self.iid_prev = None
        self.iid_next = None
        self.navigate_key = config.get("key", None)
        self.locale = locale
        self.title = config.get("title", "")
        self.type = config.get("type", "")
        self.config = config
        self.panel = panel
        self.hidden = False

    def render(self):
        raise NotImplementedError

class Entity:
    def __init__(self, locale, config, panel):
        self.iid = iid()
        self.locale = locale
        self.entity_id = config["entity"]
        self.etype = self.entity_id.split(".")[0]
        self.config = config
        self.panel = panel
        self.icon_overwrite = config.get("icon", None)
        self.name_overwrite = config.get("name", None)
        self.color_overwrite = config.get("color", None)
        self.value_overwrite = config.get("value", None)
        font_mapping = {
            "small": "1",
            "medium": "2",
            "medium-icon": "3",
            "large": "4",
        }
        self.font = font_mapping.get(config.get("font", ""), "")

    def render(self, cardType=""):
        icon_char = self.icon_overwrite or "mdi:gesture-tap-button"
        color = rgb_dec565([68, 115, 158])
        if self.color_overwrite:
            color = rgb_dec565(self.color_overwrite)
        name = self.name_overwrite or ""
        value = ""
        match self.etype:
            case 'delete':
                return f"~delete~~~~~"
            case 'navigate':
                card_iid = self.entity_id.split(".")[1]
                if card_iid == "UP":
                    return f"~button~{self.entity_id}~{get_icon_char(icon_char)}~{color}~{name}~{value}"
                else:
                    page_search_res = self.panel.searchCard(card_iid)
                    if page_search_res is not None:
                        if name == "":
                            name = page_search_res.title
                        value = get_translation(
                            self.locale, "frontend.ui.card.button.press")
                        return f"~button~{self.entity_id}~{get_icon_char(icon_char)}~{color}~{name}~{value}"
                    else:
                        return f"~text~{self.entity_id}~{get_icon_char('mdi:alert-circle-outline')}~17299~page not found~"
            case 'iText':
                # TODO: Render as HA Template
                value = self.entity_id.split(".")[1]
                return f"~text~{self.entity_id}~{get_icon_char(icon_char)}~{color}~{name}~{value}"
