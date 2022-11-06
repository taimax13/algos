## do try 1

# Print the value in `title` key.
# Print the size of `changed_files` Array.
# Print the `changed_files` Array.
# Print the `changed_files` Array in reversed order.
# Use the reversed Array and print the values of all `changed_file` keys in a new line.
# Repeat number 6 now print only the first letter.

import json 
def print_dashbord():
    payload="""{"action":"opened","number":11688,"pull_request":{"url":"https://api.github.com/repos/Monday/monday/pulls/11688","id":314120507,"state":"open","title":"Working on a new feature","user":{"login":"monday","id":10829542,"type":"User","site_admin":false},"body":"","created_at":"2019-09-04T16:23:01Z","updated_at":"2019-09-04T16:23:01Z","closed_at":null,"merged_at":null,"merged":false,"mergeable_state":"unknown","changed_lines":1024,"changed_files":[{"changed_file":"man.txt","changed_lines":822},{"changed_file":"opp.man","changed_lines":822},{"changed_file":"classic.txt","changed_lines":183},{"changed_file":"terraform.jpg","changed_lines":5678},{"changed_file":"october.tf","changed_lines":682},{"changed_file":"doc.rb","changed_lines":97},{"changed_file":"yellow.css","changed_lines":3},{"changed_file":"apple.css","changed_lines":456},{"changed_file":"direct_message.txt","changed_lines":983},{"changed_file":"no_line.gif","changed_lines":31},{"changed_file":"orange.css","changed_lines":278},{"changed_file":"main.js","changed_lines":37}]}}"""
    payload_json = json.loads(payload)
    changed_files = payload_json["pull_request"]["changed_files"]
    ##Print the value in `number` key.
    #print(payload_json["number"])
    #print(payload_json["pull_request"]["title"])
    print(len(changed_files))
    print(changed_files)
    changed_files.reverse()
    print("///////////")
    print(changed_files)
    for item in changed_files:
        print(item["changed_file"][0])




def main():
    print_dashbord()

if __name__ == '__main__':
    main()