# -*- coding: utf-8 -*-

import collections

import yaml
import rw.routing

__author__ = """Florian Ludwig"""
__email__ = 'f.ludwig@greyrook.com'
__version__ = '0.1.0'


def setup_yaml():
  """ https://stackoverflow.com/a/8661021 """
  represent_dict_order = lambda self, data:  self.represent_mapping('tag:yaml.org,2002:map', data.items())
  yaml.add_representer(collections.OrderedDict, represent_dict_order)


def _route_order_key():
    pass


def API(api_root):
    setup_yaml()
    root = rw.http.Module('swagger')

    @root.get('/')
    def get_swagger(handler):
        handler.add_header('Content-Type', 'text/yaml')

        setup_yaml()
        data = collections.OrderedDict([
            ('swagger', '2.0'),
            ('info', {
                'title': 'Titel TODO',
                'description': 'Desc TODO',
                'version': "0.0.0.todo"
            }),
            ('host', 'master.example.com'),
            ('schemes', ['https']),
            ('basePath', '/api/v1/'),
            ('produces', ['application/json']),
            ('paths', collections.OrderedDict())
        ])

        # TODO use routing table to determine basePath
        routing_table = rw.scope.get('rw.http')['routing_table']
        # print(routing_table)

        for method, path, _, fn in sorted(api_root.routes, key=lambda x: x[1]):
            route = rw.routing.parse_rule(path)
            print(route)
            path = path.replace('<', '{').replace('>', '}')
            data['paths'].setdefault(path, collections.OrderedDict())
            desc = collections.OrderedDict()
            data['paths'][path][method] = desc
            if fn.__doc__:
                desc['summary'] = fn.__doc__

            params = []
            for converter, arguments, variable in route:
                if converter is not None:
                    param = collections.OrderedDict()
                    param['name'] = variable
                    param['in'] = 'path'
                    param['required'] = True
                    param['type'] = 'string'
                    params.append(param)

            if params:
                desc['parameters'] = params

            desc['responses'] = {
                '200': {
                    'description': 'ok'
                }
            }


        handler.finish(yaml.dump(data, indent=2))

    return root
