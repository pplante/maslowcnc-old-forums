import json
import os
import operator
import datetime


def get_author_name(post):
    if 'author' not in post or post['author'] is None:
        return 'Unknown User'
    
    return post['author']['displayname']

def get_date(post):
    return datetime.datetime.fromtimestamp(post['date'])

def write_meta(fp, post):
    fp.write(f"Posted on **{get_date(post)}** by **{get_author_name(post)}**:\n\n")

def write_body(fp, post):
    fp.write(post['body'].replace('\n', '\n\n'))

def write_hr(fp):
    fp.write('\n\n---\n\n')

def write_seed(fp, post):
    fp.write(f"## {post['title']}\n")
    write_meta(fp, post)
    write_body(fp, post)
    write_hr(fp)


def write_reply(fp, post):
    write_meta(fp, post)
    write_body(fp, post)
    write_hr(fp)


if __name__ == '__main__':
    with open('maslowcnc.json', 'r') as fp:
        forums = json.load(fp)

    for category in forums['threads']:
        os.makedirs(f"output/{category}/", exist_ok=True)

        for thread in forums['threads'][category]:
            filename = f"output/{category}/{thread['seed']['key']}.md"

            with open(filename, 'w') as fp:
                write_seed(fp, thread['seed'])

                for reply in sorted(thread['replies'], key=operator.itemgetter('date')):
                    write_reply(fp, reply)
