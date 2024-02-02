"""list=[1,2,3,['yogi','rinku','rajkot','amhemdabad'],4,5]
print(len(list))
print(list[0])
print(list[3][0])
print(len(list)-2)
print(list[3][::2])
print(list[-2])

"""

# list i dictionary
"""list=[
    {
        'name':'yogita','city':'rajkot',
    },
    {
         'name':'rinku','city':'amd'
    }
]
print(list)
print(list[0]['city'])
"""
"""list=[]
n=int(input("enter number of list"))

for i in range(n):
    x=int(input("enter id"))
    a=input("enter name")
    c=input("enter city")
    l1=[x,a,c]
    list.append(l1)
    list.sort()
for i in list:
    print(i)"""

"""
string="yogita is the best "
a=string.split()
dict={}

for i in a:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
"""

list = [
  {
    "name": {
      "common": "Andorra",
      "official": "Principality of Andorra",
      "nativeName": {
        "cat": {
          "official": "Principat d'Andorra",
          "common": "Andorra"
        }
      }
    },
    "tld": [
      ".ad"
    ],
    "cca2": "AD",
    "ccn3": "020",
    "cca3": "AND",
    "cioc": "AND",
    "independent": True,
    "status": "officially-assigned",
    "unMember": True,
    "currencies": {
      "EUR": {
        "name": "Euro",
        "symbol": "€"
      }
    },
    "idd": {
      "root": "+3",
      "suffixes": [
        "76"
      ]
    },
    "capital": [
      "Andorra la Vella"
    ],
    "altSpellings": [
      "AD",
      "Principality of Andorra",
      "Principat d'Andorra"
    ],
    "region": "Europe",
    "subregion": "Southern Europe",
    "languages": {
      "cat": "Catalan"
    },
    "translations": {
      "ara": {
        "official": "إمارة أندورا",
        "common": "أندورا"
      },
      "bre": {
        "official": "Priñselezh Andorra",
        "common": "Andorra"
      },
      "ces": {
        "official": "Andorrské knížectví",
        "common": "Andorra"
      },
      "cym": {
        "official": "Tywysogaeth Andorra",
        "common": "Andorra"
      },
      "deu": {
        "official": "Fürstentum Andorra",
        "common": "Andorra"
      },
      "est": {
        "official": "Andorra Vürstiriik",
        "common": "Andorra"
      },
      "fin": {
        "official": "Andorran ruhtinaskunta",
        "common": "Andorra"
      },
      "fra": {
        "official": "Principauté d'Andorre",
        "common": "Andorre"
      },
      "hrv": {
        "official": "Kneževina Andora",
        "common": "Andora"
      },
      "hun": {
        "official": "Andorra",
        "common": "Andorra"
      },
      "ita": {
        "official": "Principato di Andorra",
        "common": "Andorra"
      },
      "jpn": {
        "official": "アンドラ公国",
        "common": "アンドラ"
      },
      "kor": {
        "official": "안도라 공국",
        "common": "안도라"
      },
      "nld": {
        "official": "Prinsdom Andorra",
        "common": "Andorra"
      },
      "per": {
        "official": "شاهزاده‌نشین آندورا",
        "common": "آندورا"
      },
      "pol": {
        "official": "Księstwo Andory",
        "common": "Andora"
      },
      "por": {
        "official": "Principado de Andorra",
        "common": "Andorra"
      },
      "rus": {
        "official": "Княжество Андорра",
        "common": "Андорра"
      },
      "slk": {
        "official": "Andorrské kniežatstvo",
        "common": "Andorra"
      },
      "spa": {
        "official": "Principado de Andorra",
        "common": "Andorra"
      },
      "srp": {
        "official": "Кнежевина Андора",
        "common": "Андора"
      },
      "swe": {
        "official": "Furstendömet Andorra",
        "common": "Andorra"
      },
      "tur": {
        "official": "Andorra Prensliği",
        "common": "Andorra"
      },
      "urd": {
        "official": "اماراتِ انڈورا",
        "common": "انڈورا"
      },
      "zho": {
        "official": "安道尔公国",
        "common": "安道尔"
      }
    },
    "latlng": [
      42.5,
      1.5
    ],
    "landlocked": True,
    "borders": [
      "FRA",
      "ESP"
    ],
    "area": 468,
    "demonyms": {
      "eng": {
        "f": "Andorran",
        "m": "Andorran"
      },
      "fra": {
        "f": "Andorrane",
        "m": "Andorran"
      }
    },
    "flag": "🇦🇩",
    "maps": {
      "googleMaps": "https://goo.gl/maps/JqAnacWE2qEznKgw7",
      "openStreetMaps": "https://www.openstreetmap.org/relation/9407"
    },
    "population": 77265,
    "fifa": "AND",
    "car": {
      "signs": [
        "AND"
      ],
      "side": "right"
    },
    "timezones": [
      "UTC+01:00"
    ],
    "continents": [
      "Europe"
    ],
    "flags": {
      "png": "https://flagcdn.com/w320/ad.png",
      "svg": "https://flagcdn.com/ad.svg",
      "alt": "The flag of Andorra features three equal vertical bands of blue, yellow and red, with the coat of arms of Andorra centered in the yellow band."
    },
    "coatOfArms": {
      "png": "https://mainfacts.com/media/images/coats_of_arms/ad.png",
      "svg": "https://mainfacts.com/media/images/coats_of_arms/ad.svg"
    },
    "startOfWeek": "monday",
    "capitalInfo": {
      "latlng": [
        42.5,
        1.52
      ]
    },
    "postalCode": {
      "format": "AD###",
      "regex": "^(?:AD)*(\\d{3})$"
    }
  }
]
   


official_value = list[0]["name"]["official"]
flag_value = list[0]["flag"]
region_value = list[0]["region"]


print(official_value)
print(flag_value)
print(region_value)

