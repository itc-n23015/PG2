import random

def generateCoinflip(length):
    """ランダムな裏表の列を生成する関数。"""
    return [random.choice(['H', 'T']) for _ in range(length)]

def coinflip(flips):
    """6連続で同じ値が続く箇所を見つける関数。"""
    for i in range(len(flips) - 5):
        if flips[i:i+6] == ['H'] * 6 or flips[i:i+6] == ['T'] * 6:
            return True
    return False

def simulate(n_simulations, sequence_length):
    """シミュレーション実行"""
    count = 0
    for _ in range(n_simulations):
        flips = generateCoinflip(sequence_length)
        if coinflip(flips):
            count += 1
    return count / n_simulations

#定数の設定
N_SIMULATIONS = 1000000
SEQUENCE_LENGTH = 100  # 任意の長さ

# シミュレーションの実行
result = simulate(N_SIMULATIONS, SEQUENCE_LENGTH)
print(f"同じ面が6連続出現する確率: {result * 100}%")






