import os
import sys
import json

def main():
    if len(sys.argv) < 2:
        print("No data provided.")
        return

    try:
        payload = json.loads(sys.argv[1])
        users = payload.get("user")
        data_payload = payload.get("data")

        if not users or data_payload is None:
            print("Invalid payload.")
            return

        # 确保所有列表长度一致
        list_lengths = [len(users)]
        for value in data_payload.values():
            list_lengths.append(len(value))
        
        if len(set(list_lengths)) != 1:
            print("All lists must have the same length.")
            return

        data_dir = 'data'
        os.makedirs(data_dir, exist_ok=True)

        # 遍历处理每组数据
        for index in range(len(users)):
            user_id = users[index]
            data = {key: values[index] for key, values in data_payload.items()}
            
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
