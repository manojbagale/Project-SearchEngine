import json
import re
import requests

ADVANCED = \
  "Any advanced searches?\n" \
  "1. Article title length\n" \
  "2. Number of articles\n" \
  "3. Get one random article\n" \
  "4. Check whether favorite article in list\n" \
  "5. Multiple keywords\n" \
  "6. None\n" \
  "Please enter a number corresponding to which advanced search you would like to perform: "

ADVANCED_TO_QUESTION = {
  1: "What's the max article title length (in number of characters) you're looking for? ",
  2: "What's the max number of articles you would like? ",
  3: "Please provide a random number to get a random article: ",
  4: "What's your favorite article title? ",
  5: "What's the other keyword you would like to search for? ",
  6: ""
}

BASIC = "What are you searching for? "

_WIKI_API = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&pageids={}&formatversion=2&explaintext=1"

# List of random Wikipedia page IDs
_ARTICLES = [
  {
   "title": "List of Canadian musicians",
    "contributor_username": "Bearcat",
    "id": "102873",
    "timestamp": "1181623340",
    "num_characters": "21023"
  },
  {
    "title": "French pop music",
    "contributor_username": "Brandon",
    "id": "6180884",
    "timestamp": "1172208041",
    "num_characters": "5569"
  },
  {
    "title": "Edogawa, Tokyo",
    "contributor_username": "Ciphers",
    "id": "335972",
    "timestamp": "1222607041",
    "num_characters": "4526"
  },
  {
    "title": "Noise (music)",
    "contributor_username": "Epbr123",
    "id": "87595",
    "timestamp": "1194207604",
    "num_characters": "15641"
  },
  {
    "title": "1922 in music",
    "contributor_username": "Jafeluv",
    "id": "163737",
    "timestamp": "1242717698",
    "num_characters": "11576"
  },
  {
    "title": "Ken Kennedy (computer scientist)",
    "contributor_username": "Jlalbee",
    "id": "9416375",
    "timestamp": "1246308670",
    "num_characters": "4144"
  },
  {
    "title": "1986 in music",
    "contributor_username": "Michael",
    "id": "160792",
    "timestamp": "1048918054",
    "num_characters": "6632"
  },
  {
    "title": "Spain national beach soccer team",
    "contributor_username": "Pegship",
    "id": "15103011",
    "timestamp": "1233458894",
    "num_characters": "1526"
  },
  {
    "title": "Kevin Cadogan",
    "contributor_username": "Renesis",
    "id": "1570956",
    "timestamp": "1144136316",
    "num_characters": "3917"
  },
  {
    "title": "Endogenous cannabinoid",
    "contributor_username": "RussBot",
    "id": "8016606",
    "timestamp": "1168971903",
    "num_characters": "26"
  },
  {
    "title": "2009 in music",
    "contributor_username": "SE KinG",
    "id": "18696414",
    "timestamp": "1235133583",
    "num_characters": "69451"
  },
  {
    "title": "Rock music",
    "contributor_username": "Sabrebd",
    "id": "25423",
    "timestamp": "1258069053",
    "num_characters": "119498"
  },
  {
    "title": "Medical value travel",
    "contributor_username": "Argon233",
    "id": "3189956",
    "timestamp": "1153157342",
    "num_characters": "4149"
  },
  {
    "title": "Lights (musician)",
    "contributor_username": "Espo3699",
    "id": "15801404",
    "timestamp": "1213914297",
    "num_characters": "5898"
  },
  {
    "title": "List of soul musicians",
    "contributor_username": "Ghmyrtle",
    "id": "170098",
    "timestamp": "1175455921",
    "num_characters": "4878"
  },
  {
    "title": "Human computer",
    "contributor_username": "Giftlite",
    "id": "3833695",
    "timestamp": "1248275178",
    "num_characters": "4750"
  },
  {
    "title": "Aube (musician)",
    "contributor_username": "Nihonjoe",
    "id": "2258925",
    "timestamp": "1145410600",
    "num_characters": "3152"
  },
  {
    "title": "List of overtone musicians",
    "contributor_username": "Sborsody",
    "id": "10759510",
    "timestamp": "1176928050",
    "num_characters": "2299"
  },
  {
    "title": "Black dog (ghost)",
    "contributor_username": "SmackBot",
    "id": "7137314",
    "timestamp": "1220471117",
    "num_characters": "14746"
  },
  {
    "title": "USC Trojans volleyball",
    "contributor_username": "Smuckers",
    "id": "5769756",
    "timestamp": "1218049435",
    "num_characters": "5525"
  },
  {
    "title": "Tim Arnold (musician)",
    "contributor_username": "Sohohobo",
    "id": "11484209",
    "timestamp": "1181480380",
    "num_characters": "4551"
  },
  {
    "title": "2007 Bulldogs RLFC season",
    "contributor_username": "Timmah86",
    "id": "7916044",
    "timestamp": "1177410119",
    "num_characters": "11116"
  },
  {
    "title": "Peter Brown (music industry)",
    "contributor_username": "Zephyrad",
    "id": "5777260",
    "timestamp": "1240235639",
    "num_characters": "2837"
  },
  {
    "title": "Mexican dog-faced bat",
    "contributor_username": "AnomieBOT",
    "id": "24555375",
    "timestamp": "1255316429",
    "num_characters": "1138"
  },
  {
    "title": "Embryo drawing",
    "contributor_username": "AxelBoldt",
    "id": "10273",
    "timestamp": "1034459202",
    "num_characters": "1712"
  },
  {
    "title": "Old-time music",
    "contributor_username": "Badagnani",
    "id": "479513",
    "timestamp": "1124771619",
    "num_characters": "12755"
  },
  {
    "title": "Arabic music",
    "contributor_username": "Badagnani",
    "id": "251740",
    "timestamp": "1209417864",
    "num_characters": "25114"
  },
  {
    "title": "C Sharp (programming language)",
    "contributor_username": "Eaglizard",
    "id": "2356196",
    "timestamp": "1232492672",
    "num_characters": "52364"
  },
  {
    "title": "List of Saturday Night Live musical sketches",
    "contributor_username": "Gary King",
    "id": "3181362",
    "timestamp": "1134966249",
    "num_characters": "13287"
  },
  {
    "title": "Joe Becker (musician)",
    "contributor_username": "Gary King",
    "id": "12255566",
    "timestamp": "1203234507",
    "num_characters": "5842"
  },
  {
    "title": "Will Johnson (soccer)",
    "contributor_username": "Mayumashu",
    "id": "3964439",
    "timestamp": "1218489712",
    "num_characters": "3562"
  },
  {
    "title": "Aco (musician)",
    "contributor_username": "Noodleboy",
    "id": "1018822",
    "timestamp": "1132546632",
    "num_characters": "3129"
  },
  {
    "title": "Geoff Smith (British musician)",
    "contributor_username": "Richardrj",
    "id": "4306585",
    "timestamp": "1194687509",
    "num_characters": "2043"
  },
  {
    "title": "Fiskerton, Lincolnshire",
    "contributor_username": "Snigbrook",
    "id": "4744436",
    "timestamp": "1259869948",
    "num_characters": "5853"
  },
  {
    "title": "Reflection-oriented programming",
    "contributor_username": "Soumyasch",
    "id": "4520792",
    "timestamp": "1143366937",
    "num_characters": "38"
  },
  {
    "title": "B (programming language)",
    "contributor_username": "Uvaphdman",
    "id": "4475",
    "timestamp": "1196622610",
    "num_characters": "5482"
  },
  {
    "title": "Richard Wright (musician)",
    "contributor_username": "Bdubiscool",
    "id": "19332171",
    "timestamp": "1189536295",
    "num_characters": "16185"
  },
  {
    "title": "Voice classification in non-classical music",
    "contributor_username": "Iridescent",
    "id": "14597488",
    "timestamp": "1198092852",
    "num_characters": "11280"
  },
  {
    "title": "Dalmatian (dog)",
    "contributor_username": "J. Spencer",
    "id": "19255892",
    "timestamp": "1207793294",
    "num_characters": "26582"
  },
  {
    "title": "1936 in music",
    "contributor_username": "JohnRogers",
    "id": "163570",
    "timestamp": "1243745950",
    "num_characters": "23417"
  },
  {
    "title": "Guide dog",
    "contributor_username": "Sarranduin",
    "id": "76885",
    "timestamp": "1165601603",
    "num_characters": "7339"
  },
  {
    "title": "1962 in country music",
    "contributor_username": "Briguy52748",
    "id": "2068000",
    "timestamp": "1249862464",
    "num_characters": "7954"
  },
  {
    "title": "List of dystopian music, TV programs, and games",
    "contributor_username": "Notinasnaid",
    "id": "1899265",
    "timestamp": "1165317338",
    "num_characters": "13458"
  },
  {
    "title": "Steven Cohen (soccer)",
    "contributor_username": "Scouselad10",
    "id": "5317001",
    "timestamp": "1237669593",
    "num_characters": "2117"
  },
  {
    "title": "Steve Perry (musician)",
    "contributor_username": "Woohookitty",
    "id": "1010610",
    "timestamp": "1254812045",
    "num_characters": "22204"
  },
  {
    "title": "2009 Louisiana Tech Bulldogs football team",
    "contributor_username": "AllisonFoley",
    "id": "23281761",
    "timestamp": "1245796406",
    "num_characters": "22410"
  },
  {
    "title": "David Gray (musician)",
    "contributor_username": "RattleandHum",
    "id": "876542",
    "timestamp": "1159841492",
    "num_characters": "7203"
  },
  {
    "title": "Craig Martin (soccer)",
    "contributor_username": "Darius Dhlomo",
    "id": "10118827",
    "timestamp": "1174203493",
    "num_characters": "709"
  },
  {
    "title": "Georgia Bulldogs football",
    "contributor_username": "Davidscharoun",
    "id": "2517159",
    "timestamp": "1166567889",
    "num_characters": "43718"
  },
  {
    "title": "Time travel",
    "contributor_username": "Thug outlaw69",
    "id": "31591",
    "timestamp": "1140826049",
    "num_characters": "35170"
  },
  {
    "title": "Fisk University",
    "contributor_username": "NerdyScienceDude",
    "id": "189946",
    "timestamp": "1263393671",
    "num_characters": "16246"
  },
  {
    "title": "Annie (musical)",
    "contributor_username": "Piano non troppo",
    "id": "357505",
    "timestamp": "1223619626",
    "num_characters": "27558"
  },
  {
    "title": "Alex Turner (musician)",
    "contributor_username": "CambridgeBayWeather",
    "id": "3003683",
    "timestamp": "1187010135",
    "num_characters": "9718"
  },
  {
    "title": "Python (programming language)",
    "contributor_username": "Lulu of the Lotus-Eaters",
    "id": "23862",
    "timestamp": "1137530195",
    "num_characters": "41571"
  },
  {
    "title": "List of gospel musicians",
    "contributor_username": "Absolon",
    "id": "179191",
    "timestamp": "1197658845",
    "num_characters": "3805"
  },
  {
    "title": "Tom Hooper (musician)",
    "contributor_username": "Bearcat",
    "id": "1283174",
    "timestamp": "1204967541",
    "num_characters": "1441"
  },
  {
    "title": "Endoglin",
    "contributor_username": "DOI bot",
    "id": "6732448",
    "timestamp": "1212259031",
    "num_characters": "6778"
  },
  {
    "title": "Indian classical music",
    "contributor_username": "Davydog",
    "id": "223014",
    "timestamp": "1222543238",
    "num_characters": "9503"
  },
  {
    "title": "Sun dog",
    "contributor_username": "Hellbus",
    "id": "323221",
    "timestamp": "1208969289",
    "num_characters": "18050"
  },
  {
    "title": "1996 in music",
    "contributor_username": "Kharker",
    "id": "160807",
    "timestamp": "1148585201",
    "num_characters": "21688"
  },
  {
    "title": "Lua (programming language)",
    "contributor_username": "Makkuro",
    "id": "46150",
    "timestamp": "1113957128",
    "num_characters": "0"
  },
  {
    "title": "Single-board computer",
    "contributor_username": "Nathael",
    "id": "194424",
    "timestamp": "1220260601",
    "num_characters": "8271"
  },
  {
    "title": "Mets de Guaynabo (volleyball)",
    "contributor_username": "Osplace",
    "id": "21895213",
    "timestamp": "1239156764",
    "num_characters": "2091"
  },
  {
    "title": "United States men's national soccer team 2009 results",
    "contributor_username": "Rebajc3",
    "id": "24259281",
    "timestamp": "1252384026",
    "num_characters": "79089"
  },
  {
    "title": "Joseph Williams (musician)",
    "contributor_username": "RussBot",
    "id": "3439709",
    "timestamp": "1140752684",
    "num_characters": "4253"
  },
  {
    "title": "The Hunchback of Notre Dame (musical)",
    "contributor_username": "RussBot",
    "id": "10251273",
    "timestamp": "1192176615",
    "num_characters": "42"
  },
  {
    "title": "China national soccer team",
    "contributor_username": "Seedbot",
    "id": "12231335",
    "timestamp": "1199103839",
    "num_characters": "45"
  },
  {
    "title": "Covariance and contravariance (computer science)",
    "contributor_username": "Wakapop",
    "id": "1104704",
    "timestamp": "1167547364",
    "num_characters": "7453"
  },
  {
    "title": "English folk music (1500–1899)",
    "contributor_username": "Ashley Y",
    "id": "1138211",
    "timestamp": "1177634764",
    "num_characters": "2073"
  },
  {
    "title": "Personal computer",
    "contributor_username": "Darklock",
    "id": "18457137",
    "timestamp": "1220391790",
    "num_characters": "45663"
  },
  {
    "title": "The Mandogs",
    "contributor_username": "DerHexer",
    "id": "12746175",
    "timestamp": "1205282029",
    "num_characters": "3968"
  },
  {
    "title": "David Levi (musician)",
    "contributor_username": "DumZiBoT",
    "id": "9659487",
    "timestamp": "1212260237",
    "num_characters": "3949"
  },
  {
    "title": "Scores (computer virus)",
    "contributor_username": "LilHelpa",
    "id": "7970552",
    "timestamp": "1235850703",
    "num_characters": "2706"
  },
  {
    "title": "Digital photography",
    "contributor_username": "Mintleaf",
    "id": "3616597",
    "timestamp": "1095727840",
    "num_characters": "18093"
  },
  {
    "title": "George Crum (musician)",
    "contributor_username": "SmackBot",
    "id": "13703703",
    "timestamp": "1252996687",
    "num_characters": "3848"
  },
  {
    "title": "Solver (computer science)",
    "contributor_username": "SmackBot",
    "id": "19125134",
    "timestamp": "1253282654",
    "num_characters": "1861"
  },
  {
    "title": "Georgia Bulldogs football under Robert Winston",
    "contributor_username": "Tlmclain",
    "id": "8422002",
    "timestamp": "1166046122",
    "num_characters": "1989"
  },
  {
    "title": "Wildlife photography",
    "contributor_username": "Zargulon",
    "id": "3957571",
    "timestamp": "1165248747",
    "num_characters": "1410"
  },
  {
    "title": "Traditional Thai musical instruments",
    "contributor_username": "Badagnani",
    "id": "13619511",
    "timestamp": "1191830919",
    "num_characters": "6775"
  },
  {
    "title": "Landseer (dog)",
    "contributor_username": "Birdgirl5",
    "id": "1379724",
    "timestamp": "1231438650",
    "num_characters": "2006"
  },
  {
    "title": "Charles McPherson (musician)",
    "contributor_username": "Cosprings",
    "id": "11095669",
    "timestamp": "1255183865",
    "num_characters": "3007"
  },
  {
    "title": "Comparison of programming languages (basic instructions)",
    "contributor_username": "IanOsgood",
    "id": "14513019",
    "timestamp": "1238781354",
    "num_characters": "61644"
  },
  {
    "title": "Les Cousins (music club)",
    "contributor_username": "Rodparkes",
    "id": "7691512",
    "timestamp": "1187072433",
    "num_characters": "4926"
  },
  {
    "title": "Paul Carr (musician)",
    "contributor_username": "Snalwibma",
    "id": "18516531",
    "timestamp": "1254142018",
    "num_characters": "5716"
  },
  {
    "title": "2006 in music",
    "contributor_username": "Suduser85",
    "id": "1570433",
    "timestamp": "1171547747",
    "num_characters": "105280"
  },
  {
    "title": "Spawning (computer gaming)",
    "contributor_username": "Vendettax",
    "id": "1196080",
    "timestamp": "1176750529",
    "num_characters": "3413"
  },
  {
    "title": "Sean Delaney (musician)",
    "contributor_username": "Bestcellar",
    "id": "16023479",
    "timestamp": "1204328174",
    "num_characters": "5638"
  },
  {
    "title": "Tony Kaye (musician)",
    "contributor_username": "Bondegezou",
    "id": "447066",
    "timestamp": "1141489894",
    "num_characters": "8419"
  },
  {
    "title": "Danja (musician)",
    "contributor_username": "Crusoe8181",
    "id": "7549507",
    "timestamp": "1257155543",
    "num_characters": "6925"
  },
  {
    "title": "Ruby (programming language)",
    "contributor_username": "Hervegirod",
    "id": "25768",
    "timestamp": "1193928035",
    "num_characters": "30284"
  },
  {
    "title": "Texture (music)",
    "contributor_username": "J Lorraine",
    "id": "410850",
    "timestamp": "1161070178",
    "num_characters": "3626"
  },
  {
    "title": "List of computer role-playing games",
    "contributor_username": "Lllockwood",
    "id": "6217026",
    "timestamp": "1179441080",
    "num_characters": "43088"
  },
  {
    "title": "Register (music)",
    "contributor_username": "Hyacinth",
    "id": "612508",
    "timestamp": "1082665179",
    "num_characters": "598"
  },
  {
    "title": "Mode (computer interface)",
    "contributor_username": "Donreed",
    "id": "2311336",
    "timestamp": "1182732608",
    "num_characters": "2991"
  },
  {
    "title": "2007 in music",
    "contributor_username": "Squilly",
    "id": "6459333",
    "timestamp": "1169248845",
    "num_characters": "45652"
  },
  {
    "title": "List of video games with time travel",
    "contributor_username": "Rockfang",
    "id": "21437409",
    "timestamp": "1234110556",
    "num_characters": "2344"
  },
  {
    "title": "2008 in music",
    "contributor_username": "Ba11innnn",
    "id": "8785767",
    "timestamp": "1217641857",
    "num_characters": "107605"
  },
  {
    "title": "Semaphore (programming)",
    "contributor_username": "Edcolins",
    "id": "164557",
    "timestamp": "1144850850",
    "num_characters": "7616"
  },
  {
    "title": "Wake Forest Demon Deacons men's soccer",
    "contributor_username": "Rebajc3",
    "id": "25057749",
    "timestamp": "1260577388",
    "num_characters": "26745"
  }
]

threshold = 5

def _find_keywords(article):
  keywords = []
  count = {}
  final_count = {}

  article = re.sub('\W+',' ', article).split(' ')

  for word in article:
    count[word] = count[word] + 1 if word in count.keys() else 1

  for key, value in count.items():
    if value > threshold:
      keywords.append(key)
      final_count[key] = value

  return keywords

def _create_id_to_metadata(info):
  """Creates a dictionary of article ID to title, author, timestamp, num_characters, and list of keywords

  Args:
    info - JSON of information from BigQuery
  """
  id_to_metadata = {}
  id_set = set()
  
  for item in info:
    article_id = item.get('id')
    #if article_id in id_set:
    #  print(article_id)
    id_set.add(article_id)
    # Delete the id from the dict
    del item['id']
  
    #print(article_id)
    # Make a request to Wikipedia
    resp = requests.get(_WIKI_API.format(article_id))

    if resp.status_code == 200:
      item['keywords'] = find_keywords(resp.json().get('query').get('pages')[0].get('extract'))
      id_to_metadata[article_id] = item
  
  return id_to_metadata

def article_titles():
  """ Returns a list of article titles
  """
  return list(map(lambda article: article.get('title'), _ARTICLES))

def article_info():
  """ Returns a list of article metadata (list of lists)
  """
  return list(map(lambda article: list(article.values()), _ARTICLES))

def _count_for_titles():
  """ Returns titles that have words in other titles
  """
  count = {}
  titles = article_titles()
  for title in titles:
    title_split = title.split(' ')
    for word in title_split:
      count[word] = count[title] + 1 if title in count.keys() else 1

  for key, value in count.items():
    if value > 1:
      print(key)
  return count

def ask_search():
  return input(BASIC)

def ask_advanced_search():
  request = int(input(ADVANCED))
  answer = input(ADVANCED_TO_QUESTION[request]) if request < 6 else ''
  return [request, answer if request >= 4 else int(answer)]