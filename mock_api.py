# coding: utf-8
import datetime

def send_to_government_agency(agency_id, complaint_text):
    """
    Davlat tashkilotlari API'si o'rniga ishlaydigan namunaviy (Mock) API.
    """
    mock_agencies = {
        "vazirlik_shaharsozlik": {
            "name": "O'zbekiston Respublikasi Qurilish va uy-joy kommunal xo'jaligi vazirligi",
            "department": "Infratuzilma va yo'l ta'mirlash boshqarmasi"
        },
        "vazirlik_energetika": {
            "name": "O'zbekiston Respublikasi Energetika vazirligi",
            "department": "Elektr va gaz ta'minoti nazorati"
        },
        "hokimiyat_toshkent": {
            "name": "Toshkent shahar hokimligi",
            "department": "Obodonlashtirish va kommunal xizmat ko'rsatish departamenti"
        }
    }
    
    agency = mock_agencies.get(agency_id)
    
    if not agency:
        return {
            "status": "error",
            "code": 404,
            "message": "Bunday davlat tashkiloti ma'lumotlar bazasidan topilmadi."
        }
        
    return {
        "status": "success",
        "code": 200,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "agency_name": agency["name"],
        "assigned_department": agency["department"],
        "message": "Murojaat sun'iy intellekt tomonidan tahlil qilindi va tegishli davlat organiga muvaffaqiyatli yo'naltirildi.",
        "data": {
            "text": complaint_text
        }
    }
