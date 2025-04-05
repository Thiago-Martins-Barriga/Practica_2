POINTS = {'kill': 3, 'assist': 1, 'death': -1}

def calcular_puntos(stats):
    return (
        stats['kills'] * POINTS['kill'] +
        stats['assists'] * POINTS['assist'] +
        (POINTS['death'] if stats['deaths'] else 0)
    )

def actualizar_stats(players_stats, game_round):
    for player, stats in game_round.items():
        if player not in players_stats:
            players_stats[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp': 0, 'points': 0}
        players_stats[player]['kills'] += stats['kills']
        players_stats[player]['assists'] += stats['assists']
        players_stats[player]['deaths'] += int(stats['deaths'])
        players_stats[player]['points'] += calcular_puntos(stats)
    return players_stats

def obtener_mvp(game_round):
    return max(game_round.keys(), key=lambda p: calcular_puntos(game_round[p]))

def imprimir_ranking(players_stats, ronda=None):
    sorted_players = sorted(players_stats.items(), key=lambda x: x[1]['points'], reverse=True)
    titulo = f"Ranking ronda {ronda}" if ronda else "Ranking final"
    print(titulo + ":")
    print("Jugador\tKills\tAsistencias\tMuertes\tMVPs\tPuntos")
    print("-" * 50)
    for player, stats in sorted_players:
        print(f"{player}\t{stats['kills']}\t{stats['assists']}\t{stats['deaths']}\t{stats['mvp']}\t{stats['points']}")
    print()