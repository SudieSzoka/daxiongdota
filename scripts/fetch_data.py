import os
import sys
import json

def main():
    if len(sys.argv) < 2:
        print("No data provided.")
        return

    try:
        payload = json.loads(sys.argv[1])
        user_id = payload.get("user")
        data = payload.get("data")

        if not user_id or data is None:
            print("Invalid payload.")
            return

        data_dir = 'data'
        os.makedirs(data_dir, exist_ok=True)
        user_file = os.path.join(data_dir, f"{user_id}.json")

        if os.path.exists(user_file):
            with open(user_file, 'r', encoding='utf-8') as f:
                data_list = json.load(f)
        else:
            data_list = []

        data_list.append(data)

        with open(user_file, 'w', encoding='utf-8') as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)

        print(f"Data appended to {user_file} successfully.")

    except json.JSONDecodeError:
        print("Failed to decode JSON.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
