import requests
import json

# Сколько денег вы получаете на данный момент в Suifrens Bullshark Quest 2
# How much money you will get on this moment at Suifrens Bullshark Quest 2
# Sharks cost 8 because - https://suifrens.com/mint


def calculate_sum(data_value, price_value):
    your_summ = float(input(
        "Введите сумму которую вы вложили в этот проект (в долларах, без знака): "))  # Total deposited in this quest
    # Sum of your accounts
    your_accounts = float(input("\nВведите количество ваших аккаунтов: "))
    your_deposit = float(
        input("\nВведите среднюю сумму которую вы внесли на аккаунт в SUI: "))  # average deposited on your account
    you_will_get = ((2500000 / data_value) * your_accounts) * price_value
    total_cost_sharks = (your_accounts * 8) * price_value
    total_deposit = (your_accounts * your_deposit) * price_value
    summ = you_will_get + total_cost_sharks + total_deposit
    # You had {} - You will get {}
    print(f"Вложили: {your_summ}$ - Получим на текущий момент: {int(summ)}$")


def get_count_players():
    url = 'https://quests.mystenlabs.com/api/trpc/quest,playerCount,leaderboard?batch=1&input=%7B%220%22%3A%7B%22questId%22%3A2%7D%2C%221%22%3A%7B%22questId%22%3A2%7D%2C%222%22%3A%7B%22questId%22%3A2%7D%7D'
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    }
    q = requests.get(url, headers=headers)
    response_string = b''.join(q).decode('utf-8')
    response_json = json.loads(response_string)
    data_value = response_json[1]['result']['data']

    url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=sui&start=1&limit=10&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true"
    q = requests.get(url, headers=headers)
    response_string = b''.join(q).decode('utf-8')
    response_json = json.loads(response_string)
    price_value = response_json["data"]["marketPairs"][0]["price"]

    calculate_sum(data_value, price_value)


def main():
    get_count_players()


if __name__ == "__main__":
    main()
