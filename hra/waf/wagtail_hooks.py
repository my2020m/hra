from wagtail.core import hooks


@hooks.register('register_rich_text_features', order=1)
def register_h5_feature(features):
    try:
        h4_index = features.default_features.index('h4')
        if h4_index == (len(features.default_features) - 1):
            features.default_features.append('h5')
        else:
            features.default_features.insert(h4_index + 1, 'h5')
    except ValueError:
        pass
