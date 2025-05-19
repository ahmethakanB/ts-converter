from functools import wraps
from typing import Dict, List, Callable, Optional


def _ensure_kolon_attributelar(col: Dict) -> List[Dict]:
    """
    Ensures the 'kolonAttributelar' list exists in the column config dict.
    """
    return col.setdefault("kolonAttributelar", [])


def tabloKolonBirlestirDepo(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'tabloKolonBirlestirDepo', 'obje': {}})
        return data

    return wrapper


def tabloKolonBirlestirMalzeme(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'tabloKolonBirlestirMalzeme', 'obje': {}})
        return data

    return wrapper


def kolonAttributelarBirimAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonAttributelarBirimAttribute', 'obje': {}})
        return data

    return wrapper


def kolonIsmiAttribute(arg: Optional[str] = None):
    """
    @kolonIsmiAttribute            → obje.baslik = None
    @kolonIsmiAttribute("ÖzelBaşlık") → obje.baslik = "ÖzelBaşlık"
    """

    def decorator(fn: Callable[[], Dict]) -> Callable[[], Dict]:
        @wraps(fn)
        def wrapped():
            data = fn()
            attrs = data.setdefault("kolonAttributelar", [])
            attrs.append({
                "tipIsmi": "kolonIsmiAttribute",
                "obje": {"baslik": arg}
            })
            return data

        return wrapped

    # dekoratör direkt kullanıldıysa arg fonksiyon olur:
    if callable(arg):
        fn = arg  # tip: kolonIsmiAttribute kullanımı parametresiz
        arg = None
        return decorator(fn)
    return decorator


def kolonGizliAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonGizliAttribute', 'obje': {}})
        return data

    return wrapper


def kolonTarihFormatAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonTarihFormatAttribute', 'obje': {}})
        return data

    return wrapper


def kolonDosya(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonDosya', 'obje': {}})
        return data

    return wrapper


def kolonGoruntu(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonGoruntu', 'obje': {}})
        return data

    return wrapper


def kolonListedeVarsayilanKapaliAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonListedeVarsayilanKapaliAttribute', 'obje': {}})
        return data

    return wrapper


def kolonKalinFontAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonKalinFontAttribute', 'obje': {}})
        return data

    return wrapper


def kolonEgikFontAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonEgikFontAttribute', 'obje': {}})
        return data

    return wrapper


def kolonDahaKucukFontAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonDahaKucukFontAttribute', 'obje': {}})
        return data

    return wrapper


def kolonDahaBuyukFontAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonDahaBuyukFontAttribute', 'obje': {}})
        return data

    return wrapper


def kolonFontRenkTuruAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonFontRenkTuruAttribute', 'obje': {}})
        return data

    return wrapper


def kolonDegerRenkAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonDegerRenkAttribute', 'obje': {}})
        return data

    return wrapper


def kolonTagGorunumAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonTagGorunumAttribute', 'obje': {}})
        return data

    return wrapper


def kolonFiltreAcikAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonFiltreAcikAttribute', 'obje': {}})
        return data

    return wrapper


def kolonFiltreKapaliAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonFiltreKapaliAttribute', 'obje': {}})
        return data

    return wrapper


def filtreNullOlamaz(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'filtreNullOlamaz', 'obje': {}})
        return data

    return wrapper


def filtreVarsayilanDeger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'filtreVarsayilanDeger', 'obje': {}})
        return data

    return wrapper


def filtreVarsayilanGorunurAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'filtreVarsayilanGorunurAttribute', 'obje': {}})
        return data

    return wrapper


def filtreSayiAralik(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'filtreSayiAralik', 'obje': {}})
        return data

    return wrapper


def filtreSayiAralikSurgu(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'filtreSayiAralikSurgu', 'obje': {}})
        return data

    return wrapper


def ondalikBasamakSayisi(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'ondalikBasamakSayisi', 'obje': {}})
        return data

    return wrapper


def filtreTarihAralikSurgu(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'filtreTarihAralikSurgu', 'obje': {}})
        return data

    return wrapper


def kolonFiltreIsimAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonFiltreIsimAttribute', 'obje': {}})
        return data

    return wrapper


def kolonSiralamaAcikAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonSiralamaAcikAttribute', 'obje': {}})
        return data

    return wrapper


def kolonSiralamaYokAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonSiralamaYokAttribute', 'obje': {}})
        return data

    return wrapper


def kolonSiralamalaIsimAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonSiralamalaIsimAttribute', 'obje': {}})
        return data

    return wrapper


def kolonSonunaMetinAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonSonunaMetinAttribute', 'obje': {}})
        return data

    return wrapper


def kolonBasinaMetinAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonBasinaMetinAttribute', 'obje': {}})
        return data

    return wrapper


def bilgilerdeAcikAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'bilgilerdeAcikAttribute', 'obje': {}})
        return data

    return wrapper


def bilgilerdeKapaliAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'bilgilerdeKapaliAttribute', 'obje': {}})
        return data

    return wrapper


def listedeAcikAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'listedeAcikAttribute', 'obje': {}})
        return data

    return wrapper


def listedeKapaliAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'listedeKapaliAttribute', 'obje': {}})
        return data

    return wrapper


def duzenledeAcikAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'duzenledeAcikAttribute', 'obje': {}})
        return data

    return wrapper


def duzenleEkBilgideKapaliAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'duzenleEkBilgideKapaliAttribute', 'obje': {}})
        return data

    return wrapper


def duzenleEkBilgideAcikAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'duzenleEkBilgideAcikAttribute', 'obje': {}})
        return data

    return wrapper


def birincilAnahtarAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'birincilAnahtarAttribute', 'obje': {}})
        return data

    return wrapper


def kolonAlanSecimEtiketAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonAlanSecimEtiketAttribute', 'obje': {}})
        return data

    return wrapper


def kolonExcelAlanSecimEtiketAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonExcelAlanSecimEtiketAttribute', 'obje': {}})
        return data

    return wrapper


def kolonAlanSecimPasifAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonAlanSecimPasifAttribute', 'obje': {}})
        return data

    return wrapper


def kolonAlanSecimSilinmisAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonAlanSecimSilinmisAttribute', 'obje': {}})
        return data

    return wrapper


def kolonAlanSecimAciklamaAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonAlanSecimAciklamaAttribute', 'obje': {}})
        return data

    return wrapper


def ogeDegistirilemezAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'ogeDegistirilemezAttribute', 'obje': {}})
        return data

    return wrapper


def formAyracAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'formAyracAttribute', 'obje': {}})
        return data

    return wrapper


def uzunMetinAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'uzunMetinAttribute', 'obje': {}})
        return data

    return wrapper


def kolonVarsayilanSiralamaAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'kolonVarsayilanSiralamaAttribute', 'obje': {}})
        return data

    return wrapper


def duzSayiAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'duzSayiAttribute', 'obje': {}})
        return data

    return wrapper


def yalnizBuyukHarfAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'yalnizBuyukHarfAttribute', 'obje': {}})
        return data

    return wrapper


def yalnizIngilizceKarakterVeSayiAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'yalnizIngilizceKarakterVeSayiAttribute', 'obje': {}})
        return data

    return wrapper


def regexKontrolAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'regexKontrolAttribute', 'obje': {}})
        return data

    return wrapper


def baglantiliAlanAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'baglantiliAlanAttribute', 'obje': {}})
        return data

    return wrapper


def zorunluFiltreAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'zorunluFiltreAttribute', 'obje': {}})
        return data

    return wrapper


def iKomutBilgiAkisTipi(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'iKomutBilgiAkisTipi', 'obje': {}})
        return data

    return wrapper


def satirEklenemez(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'satirEklenemez', 'obje': {}})
        return data

    return wrapper


def satirSilinemez(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'satirSilinemez', 'obje': {}})
        return data

    return wrapper


def sayfaliYapiKapali(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'sayfaliYapiKapali', 'obje': {}})
        return data

    return wrapper


def sorguFiltreKapali(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'sorguFiltreKapali', 'obje': {}})
        return data

    return wrapper


def dtoFiltreKapali(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'dtoFiltreKapali', 'obje': {}})
        return data

    return wrapper


def iDokumanTablosuAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'iDokumanTablosuAttribute', 'obje': {}})
        return data

    return wrapper


def tabloKolonBirlestirAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'tabloKolonBirlestirAttribute', 'obje': {}})
        return data

    return wrapper


def istekIsmiAttribute(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        data = fn(*args, **kwargs)
        lst = _ensure_kolon_attributelar(data)
        lst.append({'tipIsmi': 'istekIsmiAttribute', 'obje': {}})
        return data

    return wrapper
