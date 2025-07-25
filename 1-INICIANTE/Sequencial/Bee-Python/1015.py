import math

def main():

    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())

    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print(f"{distancia:.4f}")

if __name__ == '__main__':
    main()
