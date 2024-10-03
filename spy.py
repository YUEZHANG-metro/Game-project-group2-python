import mysql.connector
from functions.choose_country import choose_player_country
from functions.add_player import add_player
from functions.destination_options import destination_options
from functions.get_ap_co_5 import get_ap_co_5
from functions.get_ap_co_20 import get_airport_coordinate_game_country
from functions.get_distance import get_distance
from functions.get_clue import get_clue
import os
from dotenv import load_dotenv
from mysql.connector.connection_cext import CMySQLConnection

from functions.randomize_clue import randomize_clue
from functions.get_inventor import get_inventor
from functions.generate_inventor_position import generate_inventor_position
from functions.show_inventor_info import show_inventor_info
from functions.get_initial_capa_value import get_initial_capa_value

load_dotenv()


def db_connection() -> CMySQLConnection:
    connection_1 = mysql.connector.connect(
        host=f"{os.getenv('DB_HOST')}",
        user=f"{os.getenv('DB_USER')}",
        password=f"{os.getenv('DB_PASSWORD')}",
        database=f"{os.getenv('DB_NAME')}"
    )
    # print(type(connection_1))
    return connection_1

if __name__ == "__main__":
    connection = db_connection()
    player_name = input("Enter player name: ")
    current_coordinate = []

    player_country_options = choose_player_country(connection)
    player_country_id = int(input('Enter number to choose your country (1-5): '))

    # to get player's initial coordinate after they choose their home country
    initial_ap_co = get_ap_co_5(connection, player_country_id)

    # set the initial carbon_limit (for now every player is the same)
    carbon_limit = 500
    add_player(connection,player_name,player_country_id,carbon_limit)

    destinations = destination_options(connection)
    #ask user to type 1-20 to choose the next destination
    #through country info to find the target airport in that country and get the lng and lat
    choose_destination = player_country_id
    destination_airport_coordinate = get_airport_coordinate_game_country(connection,choose_destination)
    # add current airport coordinate as current player coordinate
    current_coordinate.append(destination_airport_coordinate)
    # firstly get the distance from the initial country to the destination country
    dis_ini = get_distance(initial_ap_co,destination_airport_coordinate)

    total_clue_point = 0
    while total_clue_point < 20:
        randomize_clue(connection)
        destinations = destination_options(connection)
        if len(destinations) >= 1:
            for game_country in destinations:
                print(f"{game_country[0]}：{game_country[2]}")
        choose_destination = int(input('Enter number to choose your next destination: '))

        new_des_airport_coordinate = get_airport_coordinate_game_country(connection,choose_destination)
        game_country_distance = get_distance(destination_airport_coordinate,new_des_airport_coordinate)

        # calculate distance between two airports
        airport_distance = get_distance(current_coordinate[-1], new_des_airport_coordinate)
        # change current
        current_coordinate.append(new_des_airport_coordinate)

        #check if the airport has clue
        clue = get_clue(connection, choose_destination)
        # Check if the clue exist in the selected country
        if clue:
            print(f"You've met {clue[2]} with {clue[1]} clue points!")
            total_clue_point += clue[1]
            print(f"Current clue point: {total_clue_point}")
            input("Press enter to continue...")
        else:
            print("You've met no one.")
            print(f"Current clue point: {total_clue_point}")
            input("Press enter to continue...")

    #after get 20 points of clue, get one inventor randomly from inventor table.
    inventor_id = get_inventor(connection)[0]
    # print(find_inventor)
    # generate a position information (at game_country)
    generate_inventor_position(connection,inventor_id)
    inventor_position = show_inventor_info(connection,inventor_id)
    print(f"You find a {inventor_position[0]} inventor team with {inventor_position[1]} capability value. Go! They are at {inventor_position[3]}.")
    input("Press enter to continue...")

    initial_capability_value = get_initial_capa_value(connection,player_name)[1]
    # number = int(initial_capability_value)
    capability_value_goal = 200
    capability_value_found= show_inventor_info(connection,inventor_id)[1]
    capability_value_left = initial_capability_value + capability_value_found - capability_value_goal
    print(capability_value_left)
    # while True:
    #     if initial_capability_value + capability_value_found - capability_value_goal >= 0:
    #         print(f'win')
    #     else:
    #         print(f'continue')




## after 20 point end loop, trigger inventor information.

## add inventor value to initial_capa_value to player_country.

## Loop: initial_capa_value > 200

## update carbon_emission
