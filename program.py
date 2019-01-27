'''
Assume everyone turn on private contributions and activity overview.
'''

from requests_html import HTMLSession


GITHUB_USERNAMES = [
    'zkan',
    'mesodiar',
    'yothinix',
    'gatukgl',
    'WiNloSt',
]

session = HTMLSession()

for username in GITHUB_USERNAMES:
    print(f'<h1>{username}</h1>')
    profile_url = f'https://github.com/{username}'
    r = session.get(profile_url)
    contribution_graph_canvas = r.html.find(
        f'div[data-url="/{username}"]',
        first=True
    )
    contribution_graph = contribution_graph_canvas.find('svg', first=True)
    print('<div>')
    print(contribution_graph.html)
    print('</div>')
