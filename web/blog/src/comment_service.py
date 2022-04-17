def find_root_comment_id(comments):
    list_id = []
    for i in comments:
        if not i['parent_comment']:
            list_id.append(i['id'])
    return list_id


def filter_comments(comments):
    filter_comment_id = find_root_comment_id(comments)
    result_comments = []
    for i in comments:
        if i['id'] in filter_comment_id:
            result_comments.append(i)
    return result_comments


def count_level(comments, all_id):
    counter = {i: 0 for i in all_id}

    def _count_level(comment, level=1):
        for com in comment:
            counter[com['id']] += level
            new_level = level
            if len(com['reply_comment']) != 0:
                new_level += 1
                _count_level(com['reply_comment'], new_level)
    _count_level(comments)

    return counter


def third_level_article_filter(comments, all_id):
    counter = count_level(comments, all_id)

    def _remove_element(comment):
        temp_comment = comment.copy()

        for com in temp_comment:
            if counter[com['id']] > 3:
                comment.remove(com)
            if len(com['reply_comment']) != 0:
                _remove_element(com['reply_comment'])
        return comment
    return _remove_element(comments)


def filter_result_of_article(raw_data):
    all_id = []
    comments = raw_data['comments']
    for i in comments:
        all_id.append(i['id'])

    comments = filter_comments(comments)
    raw_data['comments'] = third_level_article_filter(comments, all_id)
    return raw_data


def filter_third_level_comment(raw_data):
    all_id = []
    comments = raw_data['results']
    for i in comments:
        all_id.append(i['id'])

    comments = filter_comments(comments)
    counter = count_level(comments, all_id)

    result = []
    for c in raw_data['results']:
        if counter[c['id']] == 3:
            result.append(c)
    return result
