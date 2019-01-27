import os

from jinja2 import Environment, FileSystemLoader
from requests_html import HTMLSession


THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FILE = 'template_index.html'
GITHUB_USERNAMES = [
    'zkan',
    'mesodiar',
    'Thoritie',
    'sandysaille',
    'yothinix',
    'parnpresso',
    'DaisukiDaYo',
    'saowaluck',
    'gatukgl',
    'WiNloSt',
]

session = HTMLSession()

context = {
    'title': 'GitHub Contribution Acvitiy Visualizer',
    'user_activities': [],
}
for username in GITHUB_USERNAMES:
    profile_url = f'https://github.com/{username}'

    profile = {
        'username': username,
        'url': profile_url,
    }

    r = session.get(profile_url)
    contribution_graph_canvas = r.html.find(
        f'div[data-url="/{username}"]',
        first=True
    )
    contribution_graph = contribution_graph_canvas.find('svg', first=True)
    profile['graph'] = contribution_graph.html

    context['user_activities'].append(profile)


j2_env = Environment(
    loader=FileSystemLoader(THIS_DIR),
    trim_blocks=True
)
print(j2_env.get_template(TEMPLATE_FILE).render(context))
