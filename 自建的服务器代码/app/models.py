



def to_json(right_rate,pre_change):
    json_post={
        "resultcode": "200",
        "reason": "search sucessfully",
        "result": {
            'right_rate': right_rate,
            'pre_change': pre_change

            }

        }
    return json_post;