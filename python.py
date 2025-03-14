import requests

def check_connection(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully connected to {url}")
        else:
            print(f"Failed to connect. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error during connection: {e}")

if __name__ == '__main__':
    url = 'https://its.skshieldus.com/git/view-guard/ai/admin'  # 확인할 URL 입력
    check_connection(url)