#!/usr/bin/env python

import json, sys

def main():

    for line in sys.stdin:
        line = line.strip()

        data = ''
        try:
            data = json.loads(line)
        except ValueError as detail:
            continue

        if not (isinstance(data, dict)):
            ## not a dictionary, skip
            pass
        elif 'delete' in data:
            ## a delete element, skip for now.
            pass
        elif 'user' not in data:
            ## bizarre userless edge case
            pass
        else:
            if 'entities' in data and len(data['entities']['user_mentions']) > 0:
                user          = data['user']
                user_mentions = data['entities']['user_mentions']

                for u2 in user_mentions:                
                    print "\t".join([
                        user['id_str'],
                        u2['id_str'],
                        "1"
                        ])

if __name__ == '__main__':
    main()
                    
