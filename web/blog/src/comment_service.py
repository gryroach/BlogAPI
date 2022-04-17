def find_root_comment_id(comments):
    list_id = []
    for i in comments:
        if not i['parent_comment']:
            list_id.append(i['id'])
    return list_id


def third_level_filter(comments, all_id):
    counter = {i: 0 for i in all_id}

    def _count_level(comment, level):
        for com in comment:
            counter[com['id']] += level
            new_level = level
            if len(com['reply_comment']) != 0:
                new_level += 1
                _count_level(com['reply_comment'], new_level)

    def _remove_element(comment):
        temp_comment = comment.copy()

        for com in temp_comment:
            if counter[com['id']] > 3:
                comment.remove(com)
            if len(com['reply_comment']) != 0:
                _remove_element(com['reply_comment'])
        return comment

    _count_level(comments, 1)

    return _remove_element(comments)


def filter_result_of_article(raw_data):
    all_id = []
    comments = raw_data['comments']
    for i in comments:
        all_id.append(i['id'])

    filter_comment_id = find_root_comment_id(comments)
    filter_comments = []
    for i in comments:
        if i['id'] in filter_comment_id:
            filter_comments.append(i)

    raw_data['comments'] = third_level_filter(filter_comments, all_id)
    return raw_data
