import pandas as pd
import nycflights13 as flights

df_flights = flights.flights
df_flights
df_airlines = flights.airlines
df_airlines
df_airports = flights.airports
df_airports
df_planes = flights.planes
df_planes
df_weather = flights.weather
df_weather

flights_data = pd.read_csv("./data/nycflights.csv")
flights_data
#data 불러오기
flights_data = pd.read_csv("./data/nycflights.csv")
flights_data.head()
flights_data.info()

pd.unique(flights_data["carrier"]) 
#항공사 코드
# 'VX', 'DL', '9E', 'AA', 'WN', 'B6', 'EV', 'FL', 'UA', 'US', 'MQ','F9', 'YV', 'AS', 'HA', 'OO'

pd.unique(flights_data["tailnum"])
#항공기 등록번호(꼬리번호)
# array(['N626VA', 'N3760C', 'N712TW', ..., 'N720WN', 'N534US', 'N924WN'],shape=(3490,), dtype=object)

pd.unique(flights_data["flight"])
#항공편 번호
# array([ 407,  329,  422, ...,  552, 3986,  819], shape=(2951,))

pd.unique(flights_data["origin"])
#출발 공항 코드
#array(['JFK', 'LGA', 'EWR'], dtype=object)

pd.unique(flights_data["dest"])
# array(['LAX', 'SJU', 'TPA', 'ORF', 'ORD', 'HOU', 'IAD', 'MIA', 'JAX',
#        'ROC', 'RSW', 'DAY', 'ATL', 'BTV', 'BUF', 'DCA', 'FLL', 'SFO',
#        'PIT', 'PBI', 'DEN', 'CLT', 'CMH', 'LAS', 'DTW', 'BNA', 'PHL',
#        'MKE', 'DFW', 'SNA', 'CLE', 'MCO', 'BQN', 'ABQ', 'BOS', 'IAH',
#        'OMA', 'SYR', 'EGE', 'PWM', 'AUS', 'STT', 'MSY', 'CVG', 'RDU',
#        'MDW', 'IND', 'TYS', 'STL', 'TUL', 'JAC', 'SEA', 'MSP', 'BWI',
#        'SAT', 'CRW', 'BUR', 'SLC', 'CHS', 'RIC', 'SAN', 'XNA', 'MEM',
#        'SRQ', 'PHX', 'MCI', 'CAK', 'SAV', 'SDF', 'TVC', 'OAK', 'GSP',
#        'ALB', 'BDL', 'DSM', 'LGB', 'PDX', 'MSN', 'SMF', 'GRR', 'GSO',
#        'BGR', 'ACK', 'SJC', 'AVL', 'OKC', 'PVD', 'MHT', 'HNL', 'MTJ',
#        'BHM', 'PSE', 'ILM', 'MVY', 'HDN', 'BZN', 'CHO', 'CAE', 'EYW',
#        'ANC', 'MYR', 'PSP'], dtype=object), shape=(102,)



flights_data.loc[:,:].info()
#결측치 X



grouped_by_origin = flights_data.groupby("origin")
jfk_flights = grouped_by_origin.get_group("JFK") #총 10897개 
jfk_flights
# jfk_flights_destinations = jfk_flights["dest"].unique() #JFK <-> 도착지(66개)
# jfk_flights_destinations
jfk_flights["is_delayed"] = jfk_flights["arr_delay"] > 15
# array(['LAX', 'SJU', 'TPA', 'IAD', 'ROC', 'BTV', 'FLL', 'SFO', 'DEN',
#        'CLT', 'LAS', 'PHL', 'DCA', 'JAX', 'HOU', 'ABQ', 'BUF', 'EGE',
#        'AUS', 'STT', 'MSY', 'IAH', 'RDU', 'IND', 'DTW', 'SEA', 'RSW',
#        'MSP', 'BNA', 'BOS', 'BWI', 'SAT', 'ATL', 'MIA', 'BUR', 'SLC',
#        'ORD', 'CHS', 'PBI', 'PIT', 'PHX', 'MCO', 'OAK', 'CLE', 'LGB',
#        'SAN', 'SMF', 'CMH', 'RIC', 'CVG', 'SYR', 'SRQ', 'PWM', 'DFW',
#        'ORF', 'ACK', 'SJC', 'BQN', 'MKE', 'HNL', 'PDX', 'PSE', 'MVY',
#        'MCI', 'PSP', 'SDF'], dtype=object,shape=(66,))

# # JFK 출발 / 도착지 기준 평균 이상 노선만 살리기
# jfk_dst_mean = jfk_flights["dest"].value_counts().mean()  # 각 노선의 평균 편수 :약 165개
# jfk_top_dests = jfk_flights["dest"].value_counts()
# top_dest_list = jfk_top_dests[jfk_top_dests > jfk_dst_mean].index
# jfk_dest = jfk_flights[jfk_flights["dest"].isin(top_dest_list)] # 평균 미만 노선은 버리기
# jfk_dest["dest"]

# # JFK 출발 / 도착지 기준 상위 10개
jfk_top10_dest = jfk_flights["dest"].value_counts().head(10)
jfk_top10_dest_list = jfk_top10_dest.index

# jfk_dest.pivot_table(index="dest", values="flight", aggfunc="count").sort_values("flight",ascending=False) #노선별 운항 횟수
# jfk_dest.pivot_table(index="dest", values=["dep_delay", "arr_delay"], aggfunc="mean") #노선별 출발/도착 지연 시간 평균
# jfk_dest.groupby(["dest","year","month","day"])[["dep_delay", "arr_delay"]].mean() #노선별, 날짜별 출발/도착 지연 시간 평균
# jfk_dest.groupby(["dest","year","month"]).agg(avg_arr_delay =("arr_delay","mean"),avg_dep_delay =("dep_delay","mean"),delay_ratio =("is_delayed","mean")).head(12)#노선별, 날짜별 출발/도착 지연 시간 평균


# JFK 출발 / 도착지 지연정보
jfk_delay_info = (jfk_flights[jfk_flights["dest"].isin(list(jfk_top10_dest_list))]
                  .groupby("dest")[["arr_time", "arr_delay"]]
                  .mean()
                  .sort_values("arr_delay",ascending=False)
                )   
jfk_delay_info

# 계절
lights_data['is_delayed'] = flights_data['arr_delay'] > 15
conditions = [
    flights_data['month'].between(3, 5),    # 3~5월
    flights_data['month'].between(6, 8),    # 6~8월
    flights_data['month'].between(9, 11),   # 9~11월
    (flights_data['month'] == 12) | (flights_data['month'] <= 2)  # 12~2월
]
choices = [1, 2, 3, 4]
flights_data['season'] = np.select(conditions, choices)












lga_flights = grouped_by_origin.get_group("LGA") #총 10067개 
lga_flights
lga_flights_destinations = lga_flights["dest"].unique() #LGA <-> 도착지(83개)
lga_flights_destinations
# array(['ORF', 'ORD', 'MIA', 'RSW', 'ATL', 'PIT', 'PBI', 'CLT', 'CMH',
#        'DTW', 'BNA', 'DEN', 'DFW', 'CLE', 'MCO', 'BOS', 'IAH', 'SYR',
#        'MDW', 'IND', 'STL', 'ROC', 'FLL', 'RDU', 'CRW', 'TPA', 'XNA',
#        'MEM', 'SRQ', 'CAK', 'MKE', 'TVC', 'MSP', 'MSY', 'DCA', 'SAV',
#        'PHL', 'CVG', 'CHS', 'IAD', 'GSO', 'BGR', 'BTV', 'TYS', 'PWM',
#        'BUF', 'MCI', 'GRR', 'DSM', 'RIC', 'OMA', 'MHT', 'HOU', 'BHM',
#        'DAY', 'ILM', 'SDF', 'MSN', 'JAX', 'GSP', 'CHO', 'EYW', 'AVL',
#        'BWI', 'CAE'], dtype=object, shape=(65,))

# LGA 출발 비행편에서 도착지 기준 상위 10개
lga_top10_dest = lga_flights["dest"].value_counts().head(10)
lga_top10_dest_list = lga_top10_dest.index
# LGA 출발 / 도착지 지연정보
lga_delay_info = (lga_flights[lga_flights["dest"].isin(list(lga_top10_dest_list))]
                  .groupby("dest")[["arr_time", "arr_delay"]]
                  .mean()
                  .sort_values("arr_delay",ascending=False)
                )   
lga_delay_info


ewr_flights = grouped_by_origin.get_group("EWR") #총 11771개 
ewr_flights
ewr_flights_destinations = ewr_flights["dest"].unique() #EWR <-> 도착지(83개)
ewr_flights_destinations
# array(['HOU', 'JAX', 'DAY', 'BUF', 'DCA', 'ORD', 'PBI', 'MKE', 'SNA',
#        'TPA', 'LAS', 'CLT', 'DTW', 'BQN', 'CLE', 'OMA', 'MCO', 'PWM',
#        'IAD', 'ATL', 'CVG', 'FLL', 'RDU', 'DEN', 'DFW', 'LAX', 'BOS',
#        'TYS', 'STL', 'TUL', 'JAC', 'IAH', 'MIA', 'RIC', 'SAN', 'BNA',
#        'SAT', 'MDW', 'PHX', 'MCI', 'MEM', 'SEA', 'SAV', 'SDF', 'CMH',
#        'SFO', 'MSP', 'AUS', 'RSW', 'GSP', 'ALB', 'BDL', 'DSM', 'PDX',
#        'MSN', 'CHS', 'GRR', 'MSY', 'IND', 'GSO', 'BWI', 'SJU', 'XNA',
#        'ROC', 'AVL', 'OKC', 'PVD', 'SYR', 'MHT', 'BTV', 'ORF', 'MTJ',
#        'STT', 'SLC', 'PIT', 'HNL', 'EGE', 'HDN', 'BZN', 'TVC', 'CAE',
#        'ANC', 'MYR'], dtype=object, shape=(83,))

# EWR 출발 비행편에서 도착지 기준 상위 10개
ewr_top10_dest = ewr_flights["dest"].value_counts().head(10)
ewr_top10_dest_list = ewr_top10_dest.index
# EWR 출발 / 도착지 지연정보
ewr_delay_info = (ewr_flights[ewr_flights["dest"].isin(list(ewr_top10_dest_list))]
                  .groupby("dest")[["arr_time", "arr_delay"]]
                  .mean()
                  .sort_values("arr_delay",ascending=False)
                )   
ewr_delay_info