from AnalysisModel import PredictRating
import numpy as np


import requests ;
language_query = """
query languageStats($username: String!) {
  matchedUser(username: $username) {
    languageProblemCount {
      languageName
      problemsSolved
    }
  }
}
"""

problemSolvedQuery = """
query userProblemsSolved($username: String!) {
  matchedUser(username: $username) {
    submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
"""

contestRanking = """
query userContestRankingInfo($username: String!) {
  userContestRanking(username: $username) {
    attendedContestsCount
    rating
    globalRanking
    
  }
 
}
"""

url = "https://leetcode.com/graphql"
 
body = """
query skillStats($username: String!) {
  matchedUser(username: $username) {
    tagProblemCounts {
      advanced {
        
        tagName
       
        problemsSolved

       
      }
      intermediate {
       
         tagName
       
        problemsSolved
        
      }
      fundamental {
        
         tagName
       
        problemsSolved
      
      }
    }
  }
}

"""
variables = {"username": "iAmritSingh"}

body1 = """
query skillStats($username: String!) {
  matchedUser(username: $username) {
    tagProblemCounts {
      advanced {
        problemsSolved
      }
      intermediate {
        problemsSolved
      }
      fundamental {
        problemsSolved
      }
    }
  }
}

"""

calenderQuery = """
query userProfileCalendar($username: String!, $year: Int) {
  matchedUser(username: $username) {
    userCalendar(year: $year) {
      activeYears
      streak
      totalActiveDays
      
      submissionCalendar
    }
  }
}
"""


from csv import DictWriter


# Import DictWriter class from CSV module
from csv import DictWriter
 
# list of column names
field_names = ['username','total','easy','medium','hard','rating','C++','Java','Python','Python3','C','C#','JavaScript','TypeScript','PHP','Swift','Kotlin','Dart','Go','Ruby','Scala','Rust','Racket','Erlang','Elixir','MySQL','MS SQL Server','Oracle','Pandas','PostgreSQL','ranking',"Array", "String","Hash Table","Math","Dynamic Programming","Sorting","Greedy","Depth-First Search","Binary Search","Database","Breadth-First Search","Tree","Matrix", "Two Pointers", "Bit Manipulation","Binary Tree","Heap (Priority Queue)","Stack","Prefix Sum","Simulation","Graph","Design","Counting","Sliding Window","Backtracking", "Union Find","Enumeration", "Linked List", "Ordered Set", "Monotonic Stack","Trie","Number Theory", "Divide and Conquer", "Recursion", "Bitmask",  "Queue", "Binary Search Tree","Segment Tree", "Memoization", "Hash Function", "Geometry", "Binary Indexed Tree", "Topological Sort",  "String Matching","Combinatorics","Rolling Hash","Shortest Path","Game Theory","Data Stream","Interactive","Brainteaser","Monotonic Queue", "Randomized","Merge Sort", "Iterator", "Concurrency","Doubly-Linked List","Probability and Statistics","Quickselect","Bucket Sort","Suffix Array","Minimum Spanning Tree", "Counting Sort", "Shell",  "Line Sweep",  "Reservoir Sampling",   "Strongly Connected Component", "Eulerian Circuit",  "Radix Sort",  "Rejection Sampling",  "Biconnected Component",'contestAttended','streak','totalActiveDays','OurRating']

 


usernames = [
'sudhanshu_090' ,'aryansharma1606','mahadevwardule17','jamshedmd1111','Beyonder19','withaarzoo',
'anwendeng','Zeeshan_2512',
'sgallivan' ,
'uwi',
'devanshpareek' ,
'Mandar800' ,
'mandarmulay' ,
'shadowfax' ,
'Aditi_06' ,
'aditigarg_28' ,
'aditisingh23' ,
'Aditi_' ,
'Rohanfizz' ,
'ROHANCODEIT',
'Rohan1505' ,
'rohanb459' ,
'Kumari_Sunanda' ,
'SunandiniM1509' ,
'spandan611' ,
'venkatasaitanish' ,
'Tan_B' ,
'tanishq_1306' ,
'tanisha155' ,
'taniishaajain' ,
'tanishq1g' ,
'Tanish_K_' ,
'tanish27bansal' ,
'tanishqsinghai11' ,
'tanishsingla13390',
'Harshkriplani',
'HarshTekriwal',
'harsh-98',
'harshshah949494',
'Harsh23Kashyap' ,
'harsh_0412' ,
'void_harsh' ,
'kharsh032' ,
'suhani',
'jainmanisha3007',
'129ms',
'SuhaniShah',
'071_Prashant' ,
'prashant_nk' ,
'iAmritSingh',
'Prashantpx' ,
'prashant2611',
'prashanthr6789',
'prashant-31',
'prashant93y',
'Prashant06',
'Prashant-07',
'prashantkumarsingh9423',
'prashant_00',
'Prashant-Yadav',
'prashantkr',
'prashant_sriv',
'sainyamangral18',
'abhaybhat86',
'officialaadeesh76',
'sunandangupta',
'piyushag',
'Sithis',
'akki4497',
'shubhi17195',
'vivekthedev',
'MarkSPhilip31',
'anwendeng',
'lancertech6',

'Spaulding_',
'heroes3001',
'user0517qU',
'abdelazizSalah',
'Khosiyat',
'adwxith',
'Aman_Raj_Sinha',
'withaarzoo',
'azad786',
'mjgallag',
'noy25',
'Apophis29',
'Vivekkrsk',
'Ahmad_Ouda',
'Motaharozzaman1996',
'judgementdey',
'anushriphate'
]
# for i in usernames:
def getData(i):
  print(i)
  variables = {"username": i}
  advanced = []
  intermediate = []
  fundamental = []
  languages = []
  badges = []
  activeYears = []

  languageDict = {
  'C++':0,
  'Java':0,
  'Python':0,
  'Python3':0,
  'C':0,
  'C#':0,
  'JavaScript':0,
  'TypeScript':0,
  'PHP':0,
  'Swift':0,
  'Kotlin':0,
  'Dart':0,
  'Go':0,
  'Ruby':0,
  'Scala':0,
  'Rust':0,
  'Racket':0,
  'Erlang':0,
  'Elixir':0,
  'MySQL':0,
  'MS SQL Server':0,
  'Oracle':0,
  'Pandas':0,
  'PostgreSQL':0,
  }

  response = requests.get(url=url, json={"query": language_query, "variables":variables})
  r = response.json()
  r = (r['data']['matchedUser']['languageProblemCount'])
  for ir in r:
      languageDict[ir['languageName']] = ir['problemsSolved']



  response = requests.get(url=url, json={"query": problemSolvedQuery, "variables":variables})
  r = response.json()
  total = 0
  easy = 0
  medium = 0
  hard = 0
  rating = 0
  globalRanking = 0
  contestAttended = 0
  OurRating = 0
  total = (r['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'][0]['count'])
  easy = (r['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'][1]['count'])
  medium = (r['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'][2]['count'])
  hard = (r['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum'][3]['count'])



  response = requests.get(url=url, json={"query": contestRanking, "variables":variables})
  r = response.json()
  if(r['data']['userContestRanking']):
      contestAttended = r['data']['userContestRanking']['attendedContestsCount']
      rating = (r['data']['userContestRanking']['rating'])
      globalRanking = r['data']['userContestRanking']['globalRanking']


  topic = {"Array":0,
  "String":0,
  "Hash Table":0,
  "Math":0,
  "Dynamic Programming":0,
  "Sorting":0,
  "Greedy":0,
  "Depth-First Search":0,
  "Binary Search":0,
  "Database":0,
  "Breadth-First Search":0,
  "Tree":0,
  "Matrix":0,
  "Two Pointers":0,
  "Bit Manipulation":0,

  "Heap (Priority Queue)":0,
  "Stack":0,
  "Prefix Sum":0,
  "Simulation":0,
  "Graph":0,
  "Design":0,
  "Counting":0,
  "Sliding Window":0,
  "Backtracking":0,
  "Union Find":0,
  "Enumeration":0,
  "Linked List":0,
  "Ordered Set":0,
  "Monotonic Stack":0,
  "Trie":0,
  "Number Theory":0,
  "Divide and Conquer":0,
  "Recursion":0,
  "Bitmask":0,
  "Queue":0,
  "Binary Search Tree":0,
  "Segment Tree":0,
  "Memoization":0,
  "Hash Function":0,
  "Geometry":0,
  "Binary Indexed Tree":0,
  "Topological Sort":0,
  "String Matching":0,
  "Combinatorics":0,
  "Rolling Hash":0,
  "Shortest Path":0,
  "Game Theory":0,
  "Data Stream":0,
  "Interactive":0,
  "Brainteaser":0,
  "Monotonic Queue":0,
  "Randomized":0,
  "Merge Sort":0,
  "Iterator":0,
  "Concurrency":0,
  "Doubly-Linked List":0,
  "Probability and Statistics":0,
  "Quickselect":0,
  "Bucket Sort":0,
  "Suffix Array":0,
  "Minimum Spanning Tree":0,
  "Counting Sort":0,
  "Shell":0,
  "Line Sweep":0,
  "Reservoir Sampling":0,
  "Strongly Connected Component":0,
  "Eulerian Circuit":0,
  "Radix Sort":0,
  "Rejection Sampling":0,
  "Biconnected Component":0,
  "Binary Tree":0
  }


  response = requests.get(url=url, json={"query": body, "variables":variables})
  r = response.json()
  a = (r['data']['matchedUser']['tagProblemCounts']['advanced'])

  for ir in a:
      topic[ir['tagName']] = ir['problemsSolved']


  a = (r['data']['matchedUser']['tagProblemCounts']['intermediate'])
  for ir in a:
      topic[ir['tagName']] = ir['problemsSolved']

  a = (r['data']['matchedUser']['tagProblemCounts']['fundamental'])
  for ir in a:
      topic[ir['tagName']] = ir['problemsSolved']



  # response = requests.get(url=url, json={"query": badgesQuery, "variables":variables})
  # r = response.json()
  # print(r['data']['matchedUser']['badges'])
  # badges.append( r['data']['matchedUser']['badges'])



  response = requests.get(url=url, json={"query": calenderQuery, "variables":variables})
  r = response.json()
# print(r)
  activeYears.append(r['data']['matchedUser']['userCalendar']['activeYears'])
  streak = (r['data']['matchedUser']['userCalendar']['streak'])
  totalActiveDays = (r['data']['matchedUser']['userCalendar']['totalActiveDays'])



  
  dict = {'username':i,'total':total,'easy':easy,'medium':medium,'hard':hard,'rating':rating,'C++':languageDict['C++'],
  'Java':languageDict['Java'],
  'Python':languageDict['Python'],
  'Python3':languageDict['Python3'],
  'C':languageDict['C'],
  'C#':languageDict['C#'],
  'JavaScript':languageDict['JavaScript'],
  'TypeScript':languageDict['TypeScript'],
  'PHP':languageDict['PHP'],
  'Swift':languageDict['Swift'],
  'Kotlin':languageDict['Kotlin'],
  'Dart':languageDict['Dart'],
  'Go':languageDict['Go'],
  'Ruby':languageDict['Ruby'],
  'Scala':languageDict['Scala'],
  'Rust':languageDict['Rust'],
  'Racket':languageDict['Racket'],
  'Erlang':languageDict['Erlang'],
  'Elixir':languageDict['Elixir'],
  'MySQL':languageDict['MySQL'],
  'MS SQL Server':languageDict['MS SQL Server'],
  'Oracle':languageDict['Oracle'],
  'Pandas':languageDict['Pandas'],
  'PostgreSQL':languageDict['PostgreSQL'],
  'ranking':globalRanking,
  "Array":topic['Array'],
  "String":topic['String'],
  "Hash Table":topic['Hash Table'],
  "Math":topic['Math'],
  "Dynamic Programming":topic['Dynamic Programming'],
  "Sorting":topic['Sorting'],
  "Greedy":topic['Greedy'],
  "Depth-First Search":topic['Depth-First Search'],
  "Binary Search":topic['Binary Search'],
  "Database":topic['Database'],
  "Breadth-First Search":topic['Breadth-First Search'],
  "Tree":topic['Tree'],
  "Matrix":topic['Matrix'],
  "Two Pointers":topic['Two Pointers'],
  "Bit Manipulation":topic['Bit Manipulation'],
  "Binary Tree":topic['Binary Tree'],
  "Heap (Priority Queue)":topic['Heap (Priority Queue)'],
  "Stack":topic['Stack'],
  "Prefix Sum":topic['Prefix Sum'],
  "Simulation":topic['Simulation'],
  "Graph":topic['Graph'],
  "Design":topic['Design'],
  "Counting":topic['Counting'],
  "Sliding Window":topic['Sliding Window'],
  "Backtracking":topic['Backtracking'],
  "Union Find":topic['Union Find'],
  "Enumeration":topic['Enumeration'],
  "Linked List":topic['Linked List'],
  "Ordered Set":topic['Ordered Set'],
  "Monotonic Stack":topic['Monotonic Stack'],
  "Trie":topic['Trie'],
  "Number Theory":topic['Number Theory'],
  "Divide and Conquer":topic['Divide and Conquer'],
  "Recursion":topic['Recursion'],
  "Bitmask":topic['Bitmask'],
  "Queue":topic['Queue'],
  "Binary Search Tree":topic['Binary Search Tree'],
  "Segment Tree":topic['Segment Tree'],
  "Memoization":topic['Memoization'],
  "Hash Function":topic['Hash Function'],
  "Geometry":topic['Geometry'],
  "Binary Indexed Tree":topic['Binary Indexed Tree'],
  "Topological Sort":topic['Topological Sort'],
  "String Matching":topic['String Matching'],
  "Combinatorics":topic['Combinatorics'],
  "Rolling Hash":topic['Rolling Hash'],
  "Shortest Path":topic['Shortest Path'],
  "Game Theory":topic['Game Theory'],
  "Data Stream":topic['Data Stream'],
  "Interactive":topic['Interactive'],
  "Brainteaser":topic['Brainteaser'],
  "Monotonic Queue":topic['Monotonic Queue'],
  "Randomized":topic['Randomized'],
  "Merge Sort":topic['Merge Sort'],
  "Iterator":topic['Iterator'],
  "Concurrency":topic['Concurrency'],
  "Doubly-Linked List":topic['Doubly-Linked List'],
  "Probability and Statistics":topic['Probability and Statistics'],
  "Quickselect":topic['Quickselect'],
  "Bucket Sort":topic['Bucket Sort'],
  "Suffix Array":topic['Suffix Array'],
  "Minimum Spanning Tree":topic['Minimum Spanning Tree'],
  "Counting Sort":topic['Counting Sort'],
  "Shell":topic['Shell'],
  "Line Sweep":topic['Line Sweep'],
  "Reservoir Sampling":topic['Reservoir Sampling'],
  "Strongly Connected Component":topic['Strongly Connected Component'],
  "Eulerian Circuit":topic['Eulerian Circuit'],
  "Radix Sort":topic['Radix Sort'],
  "Rejection Sampling":topic['Rejection Sampling'],
  "Biconnected Component":topic['Biconnected Component'],'contestAttended':contestAttended,'streak':streak,'totalActiveDays':totalActiveDays,'OurRating':OurRating}

  # to be add later
  # 'badges':badges,'activeYears':activeYears,
  keys_to_eliminate = ['username', 'OurRating']

# Create a new dictionary by eliminating keys
  new_dict = {key: value for key, value in dict.items() if key not in keys_to_eliminate}
  OurRating = PredictRating(new_dict)
  int_list = OurRating.tolist()
  
  # print(int_list[0])

  dict['OurRating'] = int(int_list[0])

  with open('Leetcode.csv', 'a') as f_object:

      dictwriter_object = DictWriter(f_object, fieldnames=field_names)
      #,extrasaction='ignore'


      dictwriter_object.writerow(dict)


      f_object.close()
  


# getData("Harsh077777")