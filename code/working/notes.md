# Notes

## Temlate Languages: A comparison

### Jinja

Most commonly used template language for Flask.

Example case:

```html
{% if not categories %}

    <div>
        No Categories
    </div>

{% endif %}

{% if categories %}

    {% for c in categories %}
        <div>
            <a href="/category/{{ c.name.lower() }}"><img src="{{ c.image }}"/></a>
            <a href="/category/{{ c.name.lower() }}">{{ c.name }}</a>
        </div>

    {% endfor %}
{% endif %}
```

### Mako

Similar to Jinja with less curly brackets.

Example case:

```html
% if not categories:

    <div>
        No Categories
    </div>

% endif

% if categories:

    % for c in categories:
        <div>
            <a href="/category/${ c.get('name').lower() }"><img src="${ c.get('image') }"/></a>
            <a href="/category/${ c.get('name').lower() }">${ c.get('name') }</a>
        </div>

    % endfor
% endif
```

### Chameleon

Similar to Jinja and Mako while being simpler.

```html
<div tal:condition="not categories">
    No categories
</div>

<div tal:condition="categories">

    <div tal:condition="categories">
        <a href="/category/${ c.name.lower() }"><img src="${ c.image }" /></a>
        <a href="/category/${ c.name.lower() }">${ c.name }</a>
    </div>

</div>
```