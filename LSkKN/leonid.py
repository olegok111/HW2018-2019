
def safe_int(n):
    try:
        return int(n)
    except ValueError:
        return -1


def obhod(x, y, direction=None, turns=0):
    global Map
    Map[y][x] = str(turns)
    deltas = (-1, 0, 1)
    for dx in deltas:
        for dy in deltas:
            try:
                if x+dx != -1 and y+dy != -1:
                    if (dx, dy) == direction and (safe_int(Map[y+dy][x+dx]) > turns or Map[y+dy][x+dx] == '.'):
                        obhod(x+dx, y+dy, direction, turns)
                    elif safe_int(Map[y+dy][x+dx]) > turns + 1 or Map[y+dy][x+dx] == '.':
                        obhod(x+dx, y+dy, (dx, dy), turns+1)
            except:
                pass


with open('leonid-input.txt', 'r') as infile:
    IN = infile.readlines()
    h, w = map(int, IN[0].split())
    Map = []
    for i in range(h):
        Map.append(list(IN[1+i])[:-1])
    IN = IN[h+1:]
    sx, sy = map(int, IN[0].split())
    fx, fy = map(int, IN[1].split())
    fx -= 1
    sx -= 1
    sy = h - sy
    fy = h - fy
    obhod(sx, sy)
    print(Map)
    print(safe_int(Map[fy][fx]))