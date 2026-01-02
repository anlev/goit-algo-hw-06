import networkx as nx
import matplotlib.pyplot as plt


def create_kyiv_metro_graph():
    graph = nx.Graph()

    edges = [
        # Red line
        ("Akademmistechko", "Zhytomyrska", 4),
        ("Zhytomyrska", "Sviatoshyn", 3),
        ("Sviatoshyn", "Nyvky", 2),
        ("Nyvky", "Beresteiska", 2),
        ("Beresteiska", "Shuliavska", 2),
        ("Shuliavska", "Polytechnic Institute", 2),
        ("Polytechnic Institute", "Vokzalna", 3),
        ("Vokzalna", "Universytet", 2),
        ("Universytet", "Teatralna", 1),
        ("Teatralna", "Khreshchatyk", 1),
        ("Khreshchatyk", "Arsenalna", 2),
        ("Arsenalna", "Dnipro", 3),

        # Blue line
        ("Heroiv Dnipra", "Minska", 4),
        ("Minska", "Obolon", 2),
        ("Obolon", "Pochaina", 2),
        ("Pochaina", "Tarasa Shevchenka", 2),
        ("Tarasa Shevchenka", "Kontraktova Ploshcha", 2),
        ("Kontraktova Ploshcha", "Poshtova Ploshcha", 1),
        ("Poshtova Ploshcha", "Maidan Nezalezhnosti", 1),
        ("Maidan Nezalezhnosti", "Ploshcha Lva Tolstoho", 1),
        ("Ploshcha Lva Tolstoho", "Olimpiiska", 2),
        ("Olimpiiska", "Palats Ukraina", 2),
        ("Palats Ukraina", "Lybidska", 2),
        ("Lybidska", "Demiivska", 2),
        ("Demiivska", "Holosiivska", 2),
        ("Holosiivska", "Vasylkivska", 3),
        ("Vasylkivska", "Vystavkovyi Tsentr", 3),
        ("Vystavkovyi Tsentr", "Ipodrom", 2),
        ("Ipodrom", "Teremky", 2),

        # Green line
        ("Syrets", "Dorohozhychi", 2),
        ("Dorohozhychi", "Lukianivska", 2),
        ("Lukianivska", "Zoloti Vorota", 1),
        ("Zoloti Vorota", "Palats Sportu", 1),
        ("Palats Sportu", "Klovska", 2),
        ("Klovska", "Pecherska", 2),
        ("Pecherska", "Druzhby Narodiv", 2),
        ("Druzhby Narodiv", "Vydubychi", 2),

        # Transfers
        ("Teatralna", "Zoloti Vorota", 1),
        ("Khreshchatyk", "Maidan Nezalezhnosti", 1),
        ("Ploshcha Lva Tolstoho", "Palats Sportu", 1)
    ]

    for station_a, station_b, travel_time in edges:
        graph.add_edge(
            station_a,
            station_b,
            weight=travel_time
        )

    return graph


def analyze_graph(graph):
    print("Number of stations:", graph.number_of_nodes())
    print("Number of connections:", graph.number_of_edges())
    print("\nStation degrees:")

    for station, degree in graph.degree():
        print(f"{station}: {degree}")


def visualize_graph(graph):
    pos = {
        # Red line (horizontal)
        "Akademmistechko": (-10, 0),
        "Zhytomyrska": (-9, 0),
        "Sviatoshyn": (-8, 0),
        "Nyvky": (-7, 0),
        "Beresteiska": (-6, 0),
        "Shuliavska": (-5, 0),
        "Polytechnic Institute": (-4, 0),
        "Vokzalna": (-3, 0),
        "Universytet": (-2, 0),
        "Teatralna": (-1, 0),
        "Khreshchatyk": (0, 0),
        "Arsenalna": (1, 0),
        "Dnipro": (2, 0),

        # Blue line (vertical)
        "Heroiv Dnipra": (0, 6),
        "Minska": (0, 5),
        "Obolon": (0, 4),
        "Pochaina": (0, 3),
        "Tarasa Shevchenka": (0, 2),
        "Kontraktova Ploshcha": (0, 1),
        "Poshtova Ploshcha": (0, 0.5),
        "Maidan Nezalezhnosti": (0, -0.5),
        "Ploshcha Lva Tolstoho": (0, -1.5),
        "Olimpiiska": (0, -2.5),
        "Palats Ukraina": (0, -3.5),
        "Lybidska": (0, -4.5),
        "Demiivska": (0, -5.5),
        "Holosiivska": (0, -6.5),
        "Vasylkivska": (0, -7.5),
        "Vystavkovyi Tsentr": (0, -8.5),
        "Ipodrom": (0, -9.5),
        "Teremky": (0, -10.5),

        # Green line (diagonal)
        "Syrets": (-3, 3),
        "Dorohozhychi": (-2.5, 2.5),
        "Lukianivska": (-2, 2),
        "Zoloti Vorota": (-1, 1),
        "Palats Sportu": (0.5, -1),
        "Klovska": (1, -2),
        "Pecherska": (1.5, -3),
        "Druzhby Narodiv": (2, -4),
        "Vydubychi": (2.5, -5),
    }

    red_line = [
        "Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky",
        "Beresteiska", "Shuliavska", "Polytechnic Institute",
        "Vokzalna", "Universytet", "Teatralna",
        "Khreshchatyk", "Arsenalna", "Dnipro"
    ]

    blue_line = [
        "Heroiv Dnipra", "Minska", "Obolon", "Pochaina",
        "Tarasa Shevchenka", "Kontraktova Ploshcha",
        "Poshtova Ploshcha", "Maidan Nezalezhnosti",
        "Ploshcha Lva Tolstoho", "Olimpiiska",
        "Palats Ukraina", "Lybidska", "Demiivska",
        "Holosiivska", "Vasylkivska",
        "Vystavkovyi Tsentr", "Ipodrom", "Teremky"
    ]

    green_line = [
        "Syrets", "Dorohozhychi", "Lukianivska",
        "Zoloti Vorota", "Palats Sportu", "Klovska",
        "Pecherska", "Druzhby Narodiv", "Vydubychi"
    ]

    transfer_stations = {
        "Teatralna",
        "Zoloti Vorota",
        "Khreshchatyk",
        "Maidan Nezalezhnosti",
        "Ploshcha Lva Tolstoho",
        "Palats Sportu"
    }

    plt.figure(figsize=(16, 12))

    nx.draw_networkx_nodes(
        graph,
        pos,
        nodelist=red_line,
        node_color="red",
        node_size=900,
        label="Red Line"
    )

    nx.draw_networkx_nodes(
        graph,
        pos,
        nodelist=blue_line,
        node_color="blue",
        node_size=900,
        label="Blue Line"
    )

    nx.draw_networkx_nodes(
        graph,
        pos,
        nodelist=green_line,
        node_color="green",
        node_size=900,
        label="Green Line"
    )

    nx.draw_networkx_nodes(
        graph,
        pos,
        nodelist=transfer_stations,
        node_color="gold",
        node_size=1200,
        edgecolors="black",
        label="Transfer Stations"
    )

    nx.draw_networkx_edges(graph, pos, width=2)
    nx.draw_networkx_labels(graph, pos, font_size=8)

    plt.title("Kyiv Metro (Simplified Graph Model)", fontsize=16)
    plt.legend(scatterpoints=1)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    metro_graph = create_kyiv_metro_graph()
    analyze_graph(metro_graph)
    visualize_graph(metro_graph)
