# den - density, pop - population
import json
japan = {
    "name": "Nippon",
    "islands_number": "6,852",
    "capital": "Tōkyō",
    "driving_side": "left",
    "national_language": "Japanese",
    "area": "377,975 km2",
    "currency": "Japanese yen (¥) (JPY)",
    "time_zone": "UTC+09:00 (JST)",
    "calling_code": "+81",
    "iso_code": "JP",
    "area_mi": "145,937 sq mi",
    "climate": "Predominantly temperate",
    "local_dishes": ['Sushi', 'Sashimi', 'Ramen', 'Onogiri', 'Nabe', 'Miso', 'Tempura', 'Soba', 'Yakitori', 'Kaiseki', 'Udon', 'Sukiyaki', 'Tonkatsu', 'Donburi', 'Curry'],
    "economy": ['Industry', 'Agriculture', 'Fishery', 'Services', 'Tourism', 'Science and Technology'],
    "name_kanji": "日本国",
    "capital_kanji": "東京都",
}

hokkaido = {
    "name": "Hokkaido",
    "region": "Hokkaido",
    "island": "Hokkaido",
    "capital": "Sapporo",
    "area": "83,423.84 km2",
    "area_mi": "32,210.12 sq mi",
    "climate": "Humid continental",
    "symbols": ['Bird: Tanchō', 'Flower: Hamanasu', 'Tree: Ezomatsu'],
    "local_dishes": ['Kaisen-don', 'Jingisukan', 'Uni, Ikura-don', 'Ishikari Nabe', 'Nama Uni Donburi', 'Chan Chan Yaki'],
    "economy": ['Light industry', 'Agriculture', 'Aquaculture', 'Forestry', 'Coal mining'],
    "name_kanji": "北海道",
    "capital_kanji": "札幌市",
    "iso_code": 1,
    "area_code": "011–016",
    "lines": json.load(open(f"data/stations/hokkaido.json", 'r', encoding='utf-8'))["lines"]
}

aomori = {
    "name": "Aomori",
    "region": "Tōhoku",
    "island": "Honshu",
    "capital": "Aomori",
    "area": "9,645.64 km2",
    "area_mi": "3,724.20 sq mi",
    "climate": "Humid subtropical",
    "symbols": ["Bird: Bewick's swan", 'Flower: Apple blossom', 'Tree: Hiba'],
    "local_dishes": ['Ichigoni', 'Senbei Jiru', 'Ooma Maguro'],
    "economy": ['Agriculture', 'Fishery', 'Forestry'],
    "name_kanji": "青森県",
    "capital_kanji": "青森市",
    "iso_code": 2,
    "area_code": "017",
    "lines": json.load(open(f"data/stations/aomori.json", 'r', encoding='utf-8'))["lines"]
}

iwate = {
    "name": "Iwate",
    "region": "Tōhoku",
    "island": "Honshu",
    "capital": "Morioka",
    "area": "15,275.01 km2",
    "area_mi": "5,897.71 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Green pheasant', 'Fish: Chum salmon', 'Flower: Paulownia tree', 'Tree: Nanbu red pine'],
    "local_dishes": ['Morioka Reimen', 'Morioka Jajamen', 'Wanko Soba'],
    "economy": ['Communications manufacturing', 'Animal husbandry', 'Aquaculture'],
    "name_kanji": "岩手県",
    "capital_kanji": "盛岡市",
    "iso_code": 3,
    "area_code": "019",
    "lines": json.load(open(f"data/stations/iwate.json", 'r', encoding='utf-8'))["lines"]
}

miyagi = {
    "name": "Miyagi",
    "region": "Tōhoku",
    "island": "Honshu",
    "capital": "Sendai",
    "area": "7,282.22 km2",
    "area_mi": "2,811.68 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Wild goose', 'Flower: Miyagi bush clover', 'Tree: Japanese zelkova'],
    "local_dishes": ['Gyuutan Yaki', 'Zundamochi', 'Kaki Ryori'],
    "economy": ['Fishery', 'Agriculture', 'Electronics', 'Appliances', 'Food Processing'],
    "name_kanji": "宮城県",
    "capital_kanji": "仙台市",
    "iso_code": 4,
    "area_code": "022",
    "lines": json.load(open(f"data/stations/miyagi.json", 'r', encoding='utf-8'))["lines"]
}

akita = {
    "name": "Akita",
    "region": "Tōhoku",
    "island": "Honshu",
    "capital": "Akita",
    "area": "11,637.52 km2",
    "area_mi": "4,493.27 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Copper pheasant', 'Flower: Fuki', 'Tree: Akita-sugi'],
    "local_dishes": ['Kiritanpo Nabe', 'Inaniwa Udon', 'Hata Hata Zushi'],
    "economy": ['Agriculture', 'Fishery', 'Forestry'],
    "name_kanji": "秋田県",
    "capital_kanji": "秋田市",
    "iso_code": 5,
    "area_code": "018",
    "lines": json.load(open(f"data/stations/akita.json", 'r', encoding='utf-8'))["lines"]
}

yamagata = {
    "name": "Yamagata",
    "region": "Tōhoku",
    "island": "Honshu",
    "capital": "Yamagata",
    "area": "9,325.15 km2",
    "area_mi": "3,600.46 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Mandarin duck', 'Fish: Cherry salmon', 'Flower: Safflower', 'Tree: Cherry'],
    "local_dishes": ['Imo Nabe', 'Tamago Konyaku', 'Dongara Jiru'],
    "economy": ['Fruit growing'],
    "name_kanji": "山形県",
    "capital_kanji": "山形市",
    "iso_code": 6,
    "area_code": "023",
    "lines": json.load(open(f"data/stations/yamagata.json", 'r', encoding='utf-8'))["lines"]
}

fukushima = {
    "name": "Fukushima",
    "region": "Tōhoku",
    "island": "Honshu",
    "capital": "Fukushima",
    "area": "13,783.90 km2",
    "area_mi": "5,321.99 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Narcissus flycatcher', 'Flower: Nemotoshakunage', 'Tree: Japanese zelkova'],
    "local_dishes": ['Kozuyu', 'Kenchin Udon', 'Nishin no Sanshou Zuke'],
    "economy": ['Fishery', 'Agriculture', 'Electric industry', 'Nuclear power'],
    "name_kanji": "福島県",
    "capital_kanji": "福島市",
    "iso_code": 7,
    "area_code": "024",
    "lines": json.load(open(f"data/stations/fukushima.json", 'r', encoding='utf-8'))["lines"]
}

ibaraki = {
    "name": "Ibaraki",
    "region": "Kantō",
    "island": "Honshu",
    "capital": "Mito",
    "area": "6,097.19 km2",
    "area_mi": "2,354.14 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Eurasian Skylark', 'Flower: Rose', 'Tree: Ume tree'],
    "local_dishes": ['Ankou Nabe', 'Ankou no Dobu Jiru', 'Kenchin Jiru'],
    "economy": ['Agriculture', 'Nuclear energy', 'Machining industry'],
    "name_kanji": "茨城県",
    "capital_kanji": "水戸市",
    "iso_code": 8,
    "area_code": "029",
    "lines": json.load(open(f"data/stations/ibaraki.json", 'r', encoding='utf-8'))["lines"]
}

tochigi = {
    "name": "Tochigi",
    "region": "Kantō",
    "island": "Honshu",
    "capital": "Utsunomiya",
    "area": "6,408.09 km2",
    "area_mi": "2,474.18 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Blue-and-white flycatcher', 'Flower: Yashio tsutsuji', 'Tree: Japanese horse chestnut'],
    "local_dishes": ['Shimotsukare', 'Gyouza', 'Chitake Soba'],
    "economy": ['Industrial manufacturing', 'Agriculture'],
    "name_kanji": "栃木県",
    "capital_kanji": "宇都宮市",
    "iso_code": 9,
    "area_code": "028",
    "lines": json.load(open(f"data/stations/tochigi.json", 'r', encoding='utf-8'))["lines"]
}

gunma = {
    "name": "Gunma",
    "region": "Kantō",
    "island": "Honshu",
    "capital": "Maebashi",
    "area": "6,362.28 km2",
    "area_mi": "2,456.49 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Copper pheasant', 'Fish: Sweetfish', 'Flower: Japanese azalea', 'Tree: Japanese black pine'],
    "local_dishes": ['Yaki Manjuu', 'Okkirikomi', 'Kamameshi'],
    "economy": ['Electrical equipment', 'Transport industry', 'Agriculture', 'Sericulture'],
    "name_kanji": "群馬県",
    "capital_kanji": "前橋市",
    "iso_code": 10,
    "area_code": "027",
    "lines": json.load(open(f"data/stations/gunma.json", 'r', encoding='utf-8'))["lines"]
}

saitama = {
    "name": "Saitama",
    "region": "Kantō",
    "island": "Honshu",
    "capital": "Saitama",
    "area": "3,797.75 km2",
    "area_mi": "1,466.32 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Eurasian collared dove', 'Flower: Primrose', 'Tree: Keyaki'],
    "local_dishes": ['Hiyajiru Udon', 'Igamanjuu', 'Niboutou'],
    "economy": ['Car industry', 'Agriculture'],
    "name_kanji": "埼玉県",
    "capital_kanji": "さいたま市",
    "iso_code": 11,
    "area_code": "048",
    "lines": json.load(open(f"data/stations/saitama.json", 'r', encoding='utf-8'))["lines"]
}

chiba = {
    "name": "Chiba",
    "region": "Kantō",
    "island": "Honshu",
    "capital": "Chiba",
    "area": "5,157.61 km2",
    "area_mi": "1,991.36 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Meadow bunting', 'Fish: Seabream', 'Flower: Seiyō aburana blossom', 'Tree: Kusamaki'],
    "local_dishes": ['Namerou', 'Yude Rakkasei', 'Aji no Tataki'],
    "economy": ['Brewing industry', 'Chemical industry', 'Machine industry', 'Agriculture', 'Oil', 'Steel'],
    "name_kanji": "千葉県",
    "capital_kanji": "千葉市",
    "iso_code": 12,
    "area_code": "043",
    "lines": json.load(open(f"data/stations/chiba.json", 'r', encoding='utf-8'))["lines"]
}

tokyo = {
    "name": "Tōkyō",
    "region": "Kantō",
    "island": "Honshu",
    "capital": "Shinjuku",
    "area": "2,194.07 km2",
    "area_mi": "847.14 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Black-headed gull', 'Flower: Yoshino cherry', 'Tree: Ginkgo'],
    "local_dishes": ['Monja Yaki', 'Fukagawa Don', 'Kusaya'],
    "economy": ['Finance', 'Light industry'],
    "name_kanji": "東京都",
    "capital_kanji": "新宿区",
    "iso_code": 13,
    "area_code": "03x042",
    "lines": json.load(open(f"data/stations/tokyo.json", 'r', encoding='utf-8'))["lines"]
}

kanagawa = {
    "name": "Kanagawa",
    "region": "Kantō",
    "island": "Honshu",
    "capital": "Yokohama",
    "area": "2,415.83 km2",
    "area_mi": "932.76 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Common gull', 'Flower: Golden-rayed lily', 'Tree: Ginkgo'],
    "local_dishes": ['Kaigun Kare', 'Namashirasu Don', 'Sanmamen'],
    "economy": ['Chemistry', 'Metallurgical industry', 'Transport industry', 'Electrical industry', 'Food industry'],
    "name_kanji": "神奈川県",
    "capital_kanji": "横浜市",
    "iso_code": 14,
    "area_code": "045",
    "lines": json.load(open(f"data/stations/kanagawa.json", 'r', encoding='utf-8'))["lines"]
}

niigata = {
    "name": "Niigata",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Niigata",
    "area": "12,584.18 km2",
    "area_mi": "4,858.78 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Crested ibis', 'Flower: Tulip', 'Tree: Camellia'],
    "local_dishes": ['Noppei Jiru', 'SasaDango', 'Hegi Soba'],
    "economy": ['Agriculture', 'Forestry', 'Fishery', 'Mining', 'Manufacturing'],
    "name_kanji": "新潟県",
    "capital_kanji": "新潟市",
    "iso_code": 15,
    "area_code": "25",
    "lines": json.load(open(f"data/stations/niigata.json", 'r', encoding='utf-8'))["lines"]
}

toyama = {
    "name": "Toyama",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Toyama",
    "area": "4,247.61 km2",
    "area_mi": "1,640.01 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Ptarmigan', 'Fish: Japanese amberjack', 'Flower: Tulip', 'Tree: Tateyama Cedar'],
    "local_dishes": ['Masuzushi', 'Shiro Ebi Ryori', 'Hotaru Ika Ryori'],
    "economy": ['Agriculture', 'Manufacturing', 'Energy'],
    "name_kanji": "富山県",
    "capital_kanji": "富山市",
    "iso_code": 16,
    "area_code": "076",
    "lines": json.load(open(f"data/stations/toyama.json", 'r', encoding='utf-8'))["lines"]
}

ishikawa = {
    "name": "Ishikawa",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Kanazawa",
    "area": "4,186.09 km2",
    "area_mi": "1,616.26 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Golden eagle', 'Flower: Black lily', 'Tree: Hiba'],
    "local_dishes": ['Kabura Zushi', 'Jibuni', 'Kaga Ryori'],
    "economy": ['Textile industry', 'Artificial fabrics', 'Machine industry'],
    "name_kanji": "石川県",
    "capital_kanji": "金沢市",
    "iso_code": 17,
    "area_code": "076",
    "lines": json.load(open(f"data/stations/ishikawa.json", 'r', encoding='utf-8'))["lines"]
}

fukui = {
    "name": "Fukui",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Fukui",
    "area": "4,190.49 km2",
    "area_mi": "1,617.96 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Dusky thrush', 'Flower: Narcissus', 'Tree: Pine tree'],
    "local_dishes": ['Oroshi Soba', 'Satoimo no Koroni', 'Saba no Heshiko'],
    "economy": ['Nuclear power', 'Glasses production '],
    "name_kanji": "福井県",
    "capital_kanji": "福井市",
    "iso_code": 18,
    "area_code": "077",
    "lines": json.load(open(f"data/stations/fukui.json", 'r', encoding='utf-8'))["lines"]
}

yamanashi = {
    "name": "Yamanashi",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Kōfu",
    "area": "4,465.27 km2",
    "area_mi": "1,724.05 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Uguisu', 'Flower: Fujizakura', 'Tree: Kaede'],
    "local_dishes": ['Houtou', 'Yoshida no Udon', 'Kabocha Houtou'],
    "economy": ['Jewerly', 'Robotics', 'Wine production', 'Mineral water', 'Fruit growing'],
    "name_kanji": "山梨県",
    "capital_kanji": "甲府市",
    "iso_code": 19,
    "area_code": "055",
    "lines": json.load(open(f"data/stations/yamanashi.json", 'r', encoding='utf-8'))["lines"]
}

nagano = {
    "name": "Nagano",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Nagano",
    "area": "13,561.56 km2",
    "area_mi": "5,236.15 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Rock ptarmigan', 'Flower: Gentian', 'Tree: White birch'],
    "local_dishes": ['Shinshuu Soba', 'Nozawanazuke', 'Oyaki'],
    "economy": ['Electronics', 'Information technology', 'Precision machinery', 'Agriculture', 'Tourism'],
    "name_kanji": "長野県",
    "capital_kanji": "長野市",
    "iso_code": 20,
    "area_code": "026",
    "lines": json.load(open(f"data/stations/nagano.json", 'r', encoding='utf-8'))["lines"]
}

gifu = {
    "name": "Gifu",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Gifu",
    "area": "10,621.29 km2",
    "area_mi": "4,100.90 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Rock ptarmigan', 'Fish: Ayu', 'Flower: Chinese milk vetch', 'Tree: Japanese yew'],
    "local_dishes": ['Kurikinton', 'Keichan', 'Hobamiso'],
    "economy": ['Fishery', 'Heavy industry', 'Science', 'Paper', 'Tourism'],
    "name_kanji": "岐阜県",
    "capital_kanji": "岐阜市",
    "iso_code": 21,
    "area_code": "058",
    "lines": json.load(open(f"data/stations/gifu.json", 'r', encoding='utf-8'))["lines"]
}

shizuoka = {
    "name": "Shizuoka",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Shizuoka",
    "area": "7,777.42 km2",
    "area_mi": "3,002.88 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Japanese paradise flycatcher', 'Flower: Azalea', 'Tree: Sweet osmanthus'],
    "local_dishes": ['Sakuraebi Ryouri', 'Unagi No Kabayaki', 'Shizuoka Oden'],
    "economy": ['Agriculture', 'Forestry', 'Fishery', 'Tourism'],
    "name_kanji": "静岡県",
    "capital_kanji": "静岡市",
    "iso_code": 22,
    "area_code": "054",
    "lines": json.load(open(f"data/stations/shizuoka.json", 'r', encoding='utf-8'))["lines"]
}

aichi = {
    "name": "Aichi",
    "region": "Chūbu",
    "island": "Honshu",
    "capital": "Nagoya",
    "area": "5,172.92 km2",
    "area_mi": "1,997.28 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Scops-owl', 'Fish: Kuruma prawn', 'Flower: Kakitsubata', 'Tree: Hananoki'],
    "local_dishes": ['Hitsumabushi', 'Miso Nikomi Udon', 'Tebasaki Karaage'],
    "economy": ['Heavy industry', 'Electronics', 'Transport industry'],
    "name_kanji": "愛知県",
    "capital_kanji": "名古屋市",
    "iso_code": 23,
    "area_code": "052",
    "lines": json.load(open(f"data/stations/aichi.json", 'r', encoding='utf-8'))["lines"]
}

mie = {
    "name": "Mie",
    "region": "Kansai",
    "island": "Honshu",
    "capital": "Tsu",
    "area": "5,774.41 km2",
    "area_mi": "2,229.51 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Snowy plover', 'Fish: Japanese spiny lobster', 'Flower: Iris', 'Tree: Japanese cedar'],
    "local_dishes": ['Ise Udon', 'Tekonezushi', 'Ise Ebi Ryouri'],
    "economy": ['Handicraft', 'Forestry', 'Fishery', 'Agriculture', 'Manufacturing'],
    "name_kanji": "三重県",
    "capital_kanji": "津市",
    "iso_code": 24,
    "area_code": "059",
    "lines": json.load(open(f"data/stations/mie.json", 'r', encoding='utf-8'))["lines"]
}

shiga = {
    "name": "Shiga",
    "region": "Kansai",
    "island": "Honshu",
    "capital": "Ōtsu",
    "area": "4,017.38 km2",
    "area_mi": "1,551.12 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Little grebe', 'Flower: Rhododendron', 'Tree: Japanese maple'],
    "local_dishes": ['Funazushi', 'Kamo Nabe', 'Ayu No Tsukudani'],
    "economy": ['Agriculture', 'Electronics', 'Manufacturing', 'Textile industry', 'Fishery'],
    "name_kanji": "滋賀県",
    "capital_kanji": "大津市",
    "iso_code": 25,
    "area_code": "077",
    "lines": json.load(open(f"data/stations/shiga.json", 'r', encoding='utf-8'))["lines"]
}

kyoto = {
    "name": "Kyōto",
    "region": "Kansai",
    "island": "Honshu",
    "capital": "Kyōto",
    "area": "4,612.19 km2",
    "area_mi": "1,780.78 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Streaked shearwater', 'Flower: Weeping cherry blossom', 'Tree: Kitayama Sugi'],
    "local_dishes": ['Kaiseki Ryori', 'Kyou Tsukemono', 'Obanzai'],
    "economy": ['Agriculture', 'Tourism', 'Forestry', 'Farming', 'Manufacturing'],
    "name_kanji": "京都府",
    "capital_kanji": "京都市",
    "iso_code": 26,
    "area_code": "074",
    "lines": json.load(open(f"data/stations/kyoto.json", 'r', encoding='utf-8'))["lines"]
}

osaka = {
    "name": "Ōsaka",
    "region": "Kansai",
    "island": "Honshu",
    "capital": "Ōsaka",
    "area": "1,905.14 km2",
    "area_mi": "735.58 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Bull-headed shrike', 'Flower: Japanese apricot', 'Tree: Ginkgo tree'],
    "local_dishes": ['Takoyaki', 'Okonomiyaki', 'Kitsune Udon'],
    "economy": ['Commercial sales', 'Electronics', 'Chemistry', 'Pharmaceutical', 'Heavy industry'],
    "name_kanji": "大阪府",
    "capital_kanji": "大阪市",
    "iso_code": 27,
    "area_code": "06x",
    "lines": json.load(open(f"data/stations/osaka.json", 'r', encoding='utf-8'))["lines"]
}

hyogo = {
    "name": "Hyōgo",
    "region": "Kansai",
    "island": "Honshu",
    "capital": "Kōbe",
    "area": "8,400.94 km2",
    "area_mi": "3,243.62 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Oriental white stork', 'Flower: Nojigiku', 'Tree: Camphor tree'],
    "local_dishes": ['Akashiyaki', 'Kobe Beef', 'Ikanago no kukini'],
    "economy": ['Agriculture', 'Forestry', 'Fishery', 'Heavy & Metal industry', 'Medical industry', 'IT industry', 'Sea ports'],
    "name_kanji": "兵庫県",
    "capital_kanji": "神戸市",
    "iso_code": 28,
    "area_code": "073",
    "lines": json.load(open(f"data/stations/hyogo.json", 'r', encoding='utf-8'))["lines"]
}

nara = {
    "name": "Nara",
    "region": "Kansai",
    "island": "Honshu",
    "capital": "Nara",
    "area": "3,691.09 km2",
    "area_mi": "1,425.14 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Japanese robin', 'Fish: Goldfish', 'Flower: Nara yae zakura', 'Tree: Sugi'],
    "local_dishes": ['Kaki no Ha Zushi', 'Miwa Soumen', 'Yamato no Chagayu'],
    "economy": ['Agriculture', 'Tourism', 'Archeology', 'Traditional instruments', 'Aquaculture'],
    "name_kanji": "奈良県",
    "capital_kanji": "奈良市",
    "iso_code": 29,
    "area_code": "0x74",
    "lines": json.load(open(f"data/stations/nara.json", 'r', encoding='utf-8'))["lines"]
}

wakayama = {
    "name": "Wakayama",
    "region": "Kansai",
    "island": "Honshu",
    "capital": "Wakayama",
    "area": "4,724.69 km2",
    "area_mi": "1,824.21 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Japanese white-eye', 'Flower: Ume blossom', 'Tree: Ubame oak'],
    "local_dishes": ['Kujira no Tatsuta Age', 'Meharizushi', 'Kue Nabe'],
    "economy": ['Agriculture', 'Tourism', 'Farming'],
    "name_kanji": "和歌山県",
    "capital_kanji": "和歌山市",
    "iso_code": 30,
    "area_code": "075",
    "lines": json.load(open(f"data/stations/wakayama.json", 'r', encoding='utf-8'))["lines"]
}

tottori = {
    "name": "Tottori",
    "region": "Chūgoku",
    "island": "Honshu",
    "capital": "Tottori",
    "area": "3,507.05 km2",
    "area_mi": "1,354.08 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Mandarin duck', 'Flower: Nijisseiki', 'Tree: Daisenkyaraboku'],
    "local_dishes": ['Matsubagani Ryouri', 'Kanijuu', 'Oyama Okowa'],
    "economy": ['Agriculture', 'Farming', 'Fishing', 'Seafood'],
    "name_kanji": "鳥取県",
    "capital_kanji": "鳥取市",
    "iso_code": 31,
    "area_code": "085",
    "lines": json.load(open(f"data/stations/tottori.json", 'r', encoding='utf-8'))["lines"]
}

shimane = {
    "name": "Shimane",
    "region": "Chūgoku",
    "island": "Honshu",
    "capital": "Matsue",
    "area": "6,708.24 km2",
    "area_mi": "2,590.07 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Whooper swan', 'Fish: Flying Fish', 'Flower: Moutan peony', 'Tree: Japanese black pine'],
    "local_dishes": ['Izumo Soba', 'Shijimi Jiru', 'Taimeishi'],
    "economy": ['Retail industry', 'Manufacturing industry', 'Finance'],
    "name_kanji": "島根県",
    "capital_kanji": "松江市",
    "iso_code": 32,
    "area_code": "085",
    "lines": json.load(open(f"data/stations/shimane.json", 'r', encoding='utf-8'))["lines"]
}

okayama = {
    "name": "Okayama",
    "region": "Chūgoku",
    "island": "Honshu",
    "capital": "Okayama",
    "area": "7,114.50 km2",
    "area_mi": "2,746.92 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Lesser cuckoo', 'Flower: Peach blossom', 'Tree: Red pine'],
    "local_dishes": ['Okayama Barazushi', 'Hiruzen Okowa', 'Mamakari Zushi'],
    "economy": ['Tourism', 'Automotive manufacturing', 'Agricultural machinery', 'Shipbuilding'],
    "name_kanji": "岡山県",
    "capital_kanji": "岡山市",
    "iso_code": 33,
    "area_code": "086",
    "lines": json.load(open(f"data/stations/okayama.json", 'r', encoding='utf-8'))["lines"]
}

hiroshima = {
    "name": "Hiroshima",
    "region": "Chūgoku",
    "island": "Honshu",
    "capital": "Hiroshima",
    "area": "8,479.63 km2",
    "area_mi": "3,274.00 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Red-throated diver', 'Tree: Japanese maple'],
    "local_dishes": ['Hiroshima Okonomiyaki', 'Kaki Ryouri', 'Anago Meshidon'],
    "economy": ['Tourism', 'Automobiles', 'Manufacturing'],
    "name_kanji": "広島県",
    "capital_kanji": "広島市",
    "iso_code": 34,
    "area_code": "082",
    "lines": json.load(open(f"data/stations/hiroshima.json", 'r', encoding='utf-8'))["lines"]
}

yamaguchi = {
    "name": "Yamaguchi",
    "region": "Chūgoku",
    "island": "Honshu",
    "capital": "Yamaguchi",
    "area": "6,112.30 km2",
    "area_mi": "2,359.97 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Hooded crane', 'Fish: Japanese puffer', 'Flower: Bitter summer mandarin blossom', 'Tree: Red pine tree'],
    "local_dishes": ['Fugu Ryouri', 'Fugu Sashi', 'Shirouo Ryouri'],
    "economy": ['Machine building', 'Metallurgy', 'Textile', 'Chemical products'],
    "name_kanji": "山口県",
    "capital_kanji": "山口市",
    "iso_code": 35,
    "area_code": "083",
    "lines": json.load(open(f"data/stations/yamaguchi.json", 'r', encoding='utf-8'))["lines"]
}

tokushima = {
    "name": "Tokushima",
    "region": "Shikoku",
    "island": "Shikoku",
    "capital": "Tokushima",
    "area": "4,146.80 km2",
    "area_mi": "1,601.09 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: White heron', 'Flower: Sudachi', 'Tree: Yamamomo'],
    "local_dishes": ['Sobagome Zosui', 'Tarai Udon', 'Iya Soba'],
    "economy": ['Agriculture', 'Forestry', 'Fishery'],
    "name_kanji": "徳島県",
    "capital_kanji": "徳島市",
    "iso_code": 36,
    "area_code": "088",
    "lines": json.load(open(f"data/stations/tokushima.json", 'r', encoding='utf-8'))["lines"]
}

kagawa = {
    "name": "Kagawa",
    "region": "Shikoku",
    "island": "Shikoku",
    "capital": "Takamatsu",
    "area": "1,876.77 km2",
    "area_mi": "724.62 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Lesser cuckoo', 'Flower: Olive', 'Tree: Olive'],
    "local_dishes": ['Sanuki Udon', 'Shippoku Udon', 'Iriko Meshi'],
    "economy": ['Agriculture', 'Forestry', 'Fishery', 'Manufacturing'],
    "name_kanji": "香川県",
    "capital_kanji": "高松市",
    "iso_code": 37,
    "area_code": "087",
    "lines": json.load(open(f"data/stations/kagawa.json", 'r', encoding='utf-8'))["lines"]
}

ehime = {
    "name": "Ehime",
    "region": "Shikoku",
    "island": "Shikoku",
    "capital": "Matsuyama",
    "area": "5,676.23 km2",
    "area_mi": "2,191.60 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Mammal: Japanese river otter', 'Bird: Japanese robin', 'Fish: Red sea bream', 'Flower: Satsuma mandarin', 'Tree: Pine'],
    "local_dishes": ['Uwajima Tai Meshi', 'Jakoten', 'Satsuma-jiru'],
    "economy": ['Agriculture', 'Fishery', 'Ship building', 'Chemical industry', 'Electric power'],
    "name_kanji": "愛媛県",
    "capital_kanji": "松山市",
    "iso_code": 38,
    "area_code": "089",
    "lines": json.load(open(f"data/stations/ehime.json", 'r', encoding='utf-8'))["lines"]
}

kochi = {
    "name": "Kōchi",
    "region": "Shikoku",
    "island": "Shikoku",
    "capital": "Kōchi",
    "area": "7,103.93 km2",
    "area_mi": "2,742.84 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Fairy pitta', 'Flower: Yamamomo', 'Tree: Yanase Sugi'],
    "local_dishes": ['Katsuo no Tataki', 'Sawachi Ryouri', 'Katsuo no Tosazukuri'],
    "economy": ['Oil refining', 'Spices and seafood', 'Ship building', 'Chemical industry', 'Retail', 'Electronics hardware'],
    "name_kanji": "高知県",
    "capital_kanji": "高知市",
    "iso_code": 39,
    "area_code": "088", 
    "lines": json.load(open(f"data/stations/kochi.json", 'r', encoding='utf-8'))["lines"]
}

fukuoka = {
    "name": "Fukuoka",
    "region": "Kyushu",
    "island": "Kyushu",
    "capital": "Fukuoka",
    "area": "4,986.52 km2",
    "area_mi": "1,925.31 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Japanese bush warbler', 'Flower: Ume blossom', 'Tree: Azalea'],
    "local_dishes": ['Mentaiko', 'Motsu Nabe', 'Tori no Mizutaki'],
    "economy": ['Automobiles', 'Electronics', 'Steel'],
    "name_kanji": "福岡県",
    "capital_kanji": "福岡市",
    "iso_code": 40,
    "area_code": "082",
    "lines": json.load(open(f"data/stations/fukuoka.json", 'r', encoding='utf-8'))["lines"]
}

saga = {
    "name": "Saga",
    "region": "Kyushu",
    "island": "Kyushu",
    "capital": "Saga",
    "area": "2,440.68 km2",
    "area_mi": "942.35 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Black-billed magpie', 'Flower: Camphor blossom', 'Tree: Camphor tree'],
    "local_dishes": ['Yobiko no Ika Ryouri', 'Mutsugurou no Kabayaki', 'Dagojiru'],
    "economy": ['Agriculture', 'Fishery', 'Forestry'],
    "name_kanji": "佐賀県",
    "capital_kanji": "佐賀市",
    "iso_code": 41,
    "area_code": "095",
    "lines": json.load(open(f"data/stations/saga.json", 'r', encoding='utf-8'))["lines"]
}

nagasaki = {
    "name": "Nagasaki",
    "region": "Kyushu",
    "island": "Kyushu",
    "capital": "Nagasaki",
    "area": "4,130.88 km2",
    "area_mi": "1,594.94 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Mandarin duck', 'Flower: Unzentsutsuji', 'Tree: Sawara'],
    "local_dishes": ['Sara Udon / Chanpon', 'Shippoku Ryori', 'Sasebo Burger'],
    "economy": ['Heavy industry', 'Agriculture'],
    "name_kanji": "長崎県",
    "capital_kanji": "長崎市",
    "iso_code": 42,
    "area_code": "095",
    "lines": json.load(open(f"data/stations/nagasaki.json", 'r', encoding='utf-8'))["lines"]
}

kumamoto = {
    "name": "Kumamoto",
    "region": "Kyushu",
    "island": "Kyushu",
    "capital": "Kumamoto",
    "area": "7,409.48 km2",
    "area_mi": "2,860.82 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Eurasian skylark', 'Flower: Gentian', 'Tree: Camphor tree'],
    "local_dishes": ['Basashi', 'Ikinari Dango', 'Karashirenkon'],
    "economy": ['Tourism', 'Automobiles'],
    "name_kanji": "熊本県",
    "capital_kanji": "熊本市",
    "iso_code": 43,
    "area_code": "096",
    "lines": json.load(open(f"data/stations/kumamoto.json", 'r', encoding='utf-8'))["lines"]
}

oita = {
    "name": "Ōita",
    "region": "Kyushu",
    "island": "Kyushu",
    "capital": "Ōita",
    "area": "6,340.73 km2",
    "area_mi": "2,448.17 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Japanese white-eye', 'Flower: Bungo-ume blossom', 'Tree: Bungo-ume tree'],
    "local_dishes": ['Buri no Atsumeshi', 'Gomadashi Udon', 'Tenobe Dango Jiru'],
    "economy": ['Tourism', 'Agriculture', 'Seafood', 'Forestry'],
    "name_kanji": "大分県",
    "capital_kanji": "大分市",
    "iso_code": 44,
    "area_code": "097",
    "lines": json.load(open(f"data/stations/oita.json", 'r', encoding='utf-8'))["lines"]
}

miyazaki = {
    "name": "Miyazaki",
    "region": "Kyushu",
    "island": "Kyushu",
    "capital": "Miyazaki",
    "area": "7,735.32 km2",
    "area_mi": "2,986.62 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Ijima copper pheasant', 'Flower: Hamayu', 'Tree: Phoenix palm'],
    "local_dishes": ['Miyazaki no Sumibiyaki', 'Hiyajiru', 'Chicken Nanban'],
    "economy": ['Forestry', 'Agriculture', 'Fishery', 'Forestry', 'Textile', 'Electronics'],
    "name_kanji": "宮崎県",
    "capital_kanji": "宮崎市",
    "iso_code": 45,
    "area_code": "098",
    "lines": json.load(open(f"data/stations/miyazaki.json", 'r', encoding='utf-8'))["lines"]
}

kagoshima = {
    "name": "Kagoshima",
    "region": "Kyushu",
    "island": "Kyushu",
    "capital": "Kagoshima",
    "area": "9,187.01 km2",
    "area_mi": "3,547.12 sq mi",
    "climate": "Humid subtropical",
    "symbols": ["Bird: Lidth's jay", 'Flower: Miyamakirishima', 'Tree: Camphor laurel'],
    "local_dishes": ['Tori Meshi', 'Kibinago Ryouri', 'Tonkotsu Ryouri'],
    "economy": ['Agriculture', 'Ceramic industry', 'Electronics'],
    "name_kanji": "鹿児島県",
    "capital_kanji": "鹿児島市",
    "iso_code": 46,
    "area_code": "099",
    "lines": json.load(open(f"data/stations/kagoshima.json", 'r', encoding='utf-8'))["lines"]
}

okinawa = {
    "name": "Okinawa",
    "region": "Kyushu",
    "island": "Ryukyu Islands",
    "capital": "Naha",
    "area": "2,280.98 km2",
    "area_mi": "880.69 sq mi",
    "climate": "Humid subtropical",
    "symbols": ['Bird: Okinawa woodpecker', 'Fish: Banana fish', 'Flower: Deego', 'Tree: Pinus luchuensis'],
    "local_dishes": ['Soki Soba', 'Goya Chanpuru', 'Rafutee'],
    "economy": ['Military', 'Tourism', 'Agriculture', 'Fishery', 'Retail', 'Civil engineering', 'Petroleum'],
    "name_kanji": "沖縄県",
    "capital_kanji": "那覇市",
    "iso_code": 47,
    "area_code": "098",
    "lines": json.load(open(f"data/stations/okinawa.json", 'r', encoding='utf-8'))["lines"]
}

all_prefectures = [hokkaido, aomori, iwate, miyagi, akita, yamagata, fukushima, ibaraki,
                   tochigi, gunma, saitama, chiba, tokyo, kanagawa, niigata, toyama, ishikawa,
                   fukui, yamanashi, nagano, gifu, shizuoka, aichi, mie, shiga, kyoto, osaka,
                   hyogo, nara, wakayama, tottori, shimane, okayama, hiroshima, yamaguchi, tokushima,
                   kagawa, ehime, kochi, fukuoka, saga, nagasaki, kumamoto, oita, miyazaki, kagoshima, okinawa]