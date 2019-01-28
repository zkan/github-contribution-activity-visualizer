import os

from jinja2 import Environment, FileSystemLoader
from requests_html import HTMLSession

from github import GITHUB_USERNAMES


def get_contribution_activities():
    session = HTMLSession()
    context = {
        'title': 'GitHub Contribution Activity Visualizer',
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

    return context


def render(context):
    THIS_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FILE = 'template_index.html'
    j2_env = Environment(
        loader=FileSystemLoader(THIS_DIR),
        trim_blocks=True
    )
    print(j2_env.get_template(TEMPLATE_FILE).render(context))


if __name__ == '__main__':
    context = get_contribution_activities()
    render(context)
