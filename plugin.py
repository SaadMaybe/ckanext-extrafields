# encoding: utf-8
import ckan.plugins as p
import ckan.plugins.toolkit as tk

class ExampleIDatasetFormPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)
    p.implements(p.ITemplateHelpers)
    p.implements(p.IFacets)

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')

    def create_package_schema(self):
        # let's grab the default schema in our plugin
        schema = super(ExampleIDatasetFormPlugin, self).create_package_schema()
        # our custom field
        schema.update({
        'source': [tk.get_validator('ignore_missing'),
        tk.get_converter('convert_to_extras')]
        })
        schema.update({
        'publisher': [tk.get_validator('ignore_missing'),
        tk.get_converter('convert_to_extras')]
        })
        schema.update({
        'custom_author': [tk.get_validator('ignore_missing'),
        tk.get_converter('convert_to_extras')]
        })
        schema.update({
        'categories': [
            tk.get_validator('ignore_missing'),
            tk.get_converter('convert_to_extras')
        ]
        })
        schema.update({
        'oragnization_types': [
            tk.get_validator('ignore_missing'),
            tk.get_converter('convert_to_extras')
        ]
        })
        schema.update({
        'data_types': [
            tk.get_validator('ignore_missing'),
            tk.get_converter('convert_to_extras')
        ]
        })
        schema.update({
        'data_sources': [
            tk.get_validator('ignore_missing'),
            tk.get_converter('convert_to_extras')
        ]
        })
        schema.update({
        'ODP_Pakistan': [
            tk.get_validator('ignore_missing'),
            tk.get_converter('convert_to_extras')
        ]
        })
        schema.update({
        'locations': [
            tk.get_validator('ignore_missing'),
            tk.get_converter('convert_to_extras')
        ]
        })
        schema['resources'].update({
            'datastore_active' : [ tk.get_validator('ignore_missing') ]
        })
        schema['resources'].update({
            'has_views' : [ tk.get_validator('ignore_missing') ]
        })
        schema['resources'].update({
            'mimetype' : [ tk.get_validator('ignore_missing') ]
        })

        schema['resources'].update({
            'revision_id' : [ tk.get_validator('ignore_missing') ]
        })
        return schema

    def update_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).update_package_schema()
        # our custom field
        schema.update({
        'source': [tk.get_validator('ignore_missing'),
        tk.get_converter('convert_to_extras')]
        })
        schema.update({
        'publisher': [tk.get_validator('ignore_missing'),
        tk.get_converter('convert_to_extras')]
        })
        schema.update({
        'custom_author': [tk.get_validator('ignore_missing'),
        tk.get_converter('convert_to_extras')]
        })
        schema.update({
        'categories': [
            tk.get_validator('ignore_missing'),
            tk.get_converter('convert_to_extras')
        ]
        })
        schema.update({
        'organization_types': [
            tk.get_validator('ignore_missing'),
            tk.get_converter('convert_to_extras')
        ]
        })
        schema.update({
        'data_types': [
            tk.get_validator('ignore_missing'),
            tk.get_converter('convert_to_extras')
        ]
        })
        schema.update({
        'data_sources': [
            tk.get_validator('ignore_missing'),
            tk.get_converter('convert_to_extras')
        ]
        })
        schema.update({
        'ODP_Pakistan': [
            tk.get_validator('ignore_missing'),
            tk.get_converter('convert_to_extras')
        ]
        })
        schema.update({
        'locations': [
            tk.get_validator('ignore_missing'),
            tk.get_converter('convert_to_extras')
        ]
        })
        
        schema['resources'].update({
            'datastore_active' : [ tk.get_validator('ignore_missing') ]
        })
        schema['resources'].update({
            'has_views' : [ tk.get_validator('ignore_missing') ]
        })
        schema['resources'].update({
            'mimetype' : [ tk.get_validator('ignore_missing') ]
        })
        
        schema['resources'].update({
            'revision_id' : [ tk.get_validator('ignore_missing') ]
        })
        return schema
    
    def show_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).show_package_schema()
        schema.update({
        'source': [tk.get_converter('convert_from_extras'),
        tk.get_validator('ignore_missing')]
        })
        schema.update({
        'publisher': [tk.get_converter('convert_from_extras'),tk.get_validator('ignore_missing')]
        })
        schema.update({
        'custom_author': [tk.get_converter('convert_from_extras'),tk.get_validator('ignore_missing')]
        })
        schema.update({
        'categories': [
            tk.get_converter('convert_from_extras'),
            tk.get_validator('ignore_missing')
        ]
        })
        schema.update({
        'ODP_Pakistan': [
            tk.get_converter('convert_from_extras'),
            tk.get_validator('ignore_missing')
        ]
        })
        schema.update({
        'organization_types': [
            tk.get_converter('convert_from_extras'),
            tk.get_validator('ignore_missing')
        ]
        })
        schema.update({
        'data_types': [
            tk.get_converter('convert_from_extras'),
            tk.get_validator('ignore_missing')
        ]
        })
        schema.update({
        'data_sources': [
            tk.get_converter('convert_from_extras'),
            tk.get_validator('ignore_missing')
        ]
        })
        schema.update({
        'locations': [
            tk.get_converter('convert_from_extras'),
            tk.get_validator('ignore_missing')
        ]
        })
        schema['resources'].update({
            'datastore_active' : [ tk.get_validator('ignore_missing') ]
        })
        schema['resources'].update({
            'has_views' : [ tk.get_validator('ignore_missing') ]
        })
        schema['resources'].update({
            'mimetype' : [ tk.get_validator('ignore_missing') ]
        })
        
        schema['resources'].update({
            'revision_id' : [ tk.get_validator('ignore_missing') ]
        })

        # -------------------------
        return schema

    def create_ODP_Pakistan(self):
        myVocab = (u'Public Safety', u'Economics and Finance', u'Government and Public Sector', u'Demography', u'Health', u'Environment and Energy', u'Education', u'Cities and Region', u'Housing and Public Sector', u'Connectivity', u'Agriculture Food and Forests', u'Manufacturing', u'Science and Technology', u'Culture')

        user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
        context = {'user': user['name']}
        try:
            data = {'id': 'ODP_Pakistan'}
            tag_data = {'vocabulary_id': 'ODP_Pakistan'}
            
            tk.get_action('vocabulary_show')(context, data)

            smth = tk.get_action('tag_list')(context, tag_data)
            for i in myVocab:
                if i not in smth:
                    vocabData = {"id": "ODP_Pakistan"}
                    update_vocab = tk.get_action('vocabulary_update')(context, vocabData)
                    data = {'name': i, 'vocabulary_id': update_vocab['id']}
                    tk.get_action('tag_create')(context, data)
            for i in smth:
                if i not in myVocab:
                    del_data = {"vocabulary_id": "ODP_Pakistan", "id": i}
                    update_vocab = tk.get_action('tag_delete')(context, del_data)
        except tk.ObjectNotFound:
            data = {'name': 'ODP_Pakistan'}
            vocab = tk.get_action('vocabulary_create')(context, data)
            for tag in (u'Public Safety', u'Economics and Finance', u'Government and Public Sector', u'Demography', u'Health', u'Environment and Energy', u'Education', u'Cities and Region', u'Housing and Public Sector', u'Connectivity', u'Agriculture, Food and Forests', u'Manufacturing', u'Science and Technology', u'Culture'):
                data = {'name': tag, 'vocabulary_id': vocab['id']}
                tk.get_action('tag_create')(context, data)
    
    def ODP_Pakistan(self):
        self.create_ODP_Pakistan()
        try:
            tag_list = tk.get_action('tag_list')
            ODP_Pakistan = tag_list(data_dict={'vocabulary_id': 'ODP_Pakistan'})
            return ODP_Pakistan
        except tk.ObjectNotFound:
            return None

    def create_categories(self):
        myVocab = (u'Public Safety', u'Economics and Finance', u'Government and Public Sector', u'Demography', u'Health', u'Environment and Energy', u'Education', u'Cities and Region', u'Housing and Public Sector', u'Connectivity', u'Agriculture Food and Forests', u'Manufacturing', u'Science and Technology', u'Culture')

        user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
        context = {'user': user['name']}
        try:
            data = {'id': 'categories'}
            tag_data = {'vocabulary_id': 'categories'}
            
            tk.get_action('vocabulary_show')(context, data)

            smth = tk.get_action('tag_list')(context, tag_data)
            for i in myVocab:
                if i not in smth:
                    vocabData = {"id": "categories"}
                    update_vocab = tk.get_action('vocabulary_update')(context, vocabData)
                    data = {'name': i, 'vocabulary_id': update_vocab['id']}
                    tk.get_action('tag_create')(context, data)
            for i in smth:
                if i not in myVocab:
                    del_data = {"vocabulary_id": "categories", "id": i}
                    update_vocab = tk.get_action('tag_delete')(context, del_data)
        except tk.ObjectNotFound:
            data = {'name': 'categories'}
            vocab = tk.get_action('vocabulary_create')(context, data)
            for tag in (u'Public Safety', u'Economics and Finance', u'Government and Public Sector', u'Demography', u'Health', u'Environment and Energy', u'Education', u'Cities and Region', u'Housing and Public Sector', u'Connectivity', u'Agriculture Food and Forests', u'Manufacturing', u'Science and Technology', u'Culture'):
                data = {'name': tag, 'vocabulary_id': vocab['id']}
                tk.get_action('tag_create')(context, data)
    
    def categories(self):
        self.create_categories()
        try:
            tag_list = tk.get_action('tag_list')
            categories = tag_list(data_dict={'vocabulary_id': 'categories'})
            return categories
        except tk.ObjectNotFound:
            return None

    def create_organization_types(self):
        myVocab = (u'Private Organization', u'Educational Institute', u'Federal Government', u'Other', u'NGO', u'Provincial Government')
        user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
        context = {'user': user['name']}
    

        try:
            data = {'id': 'organization_types'}
            tag_data = {'vocabulary_id': 'organization_types'}
            
            tk.get_action('vocabulary_show')(context, data)

            smth = tk.get_action('tag_list')(context, tag_data)
            for i in myVocab:
                if i not in smth:
                    vocabData = {"id": "organization_types"}
                    update_vocab = tk.get_action('vocabulary_update')(context, vocabData)
                    data = {'name': i, 'vocabulary_id': update_vocab['id']}
                    tk.get_action('tag_create')(context, data)
            for i in smth:
                if i not in myVocab:
                    del_data = {"vocabulary_id": "organization_types", "id": i}
                    update_vocab = tk.get_action('tag_delete')(context, del_data)
        except tk.ObjectNotFound:
            data = {'name': 'organization_types'}
            vocab = tk.get_action('vocabulary_create')(context, data)
            for tag in (u'Private Organization', u'Educational Institute', u'Federal Government', u'Other', u'NGO', u'Provincial Government'):
                data = {'name': tag, 'vocabulary_id': vocab['id']}
                tk.get_action('tag_create')(context, data)
    
    def organization_types(self):
        self.create_organization_types()
        try:
            tag_list = tk.get_action('tag_list')
            organization_types = tag_list(data_dict={'vocabulary_id': 'organization_types'})
            return organization_types
        except tk.ObjectNotFound:
            return None
    def create_locations(self):
        myVocab = ( u'Khyber Pakhtunkhwa Pakistan' ,u'Punjab Pakistan', u'Sindh Pakistan', u'Balochistan Pakistan', u'Federal Capital Territory', u'Gilgit Baltistan Pakistan', u'Azad Kashmir Pakistan', u'Islamabad Federal Capital Territory', u'Lahore Punjab' ,u'Islamabad Islamabad Federal Capital Territory', u'Karachi City Sindh', u'Peshawar Khyber Pakhtunkhwa')
        user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
        context = {'user': user['name']}
    

        try:
            data = {'id': 'locations'}
            tag_data = {'vocabulary_id': 'locations'}
            
            tk.get_action('vocabulary_show')(context, data)

            smth = tk.get_action('tag_list')(context, tag_data)
            for i in myVocab:
                if i not in smth:
                    vocabData = {"id": "locations"}
                    update_vocab = tk.get_action('vocabulary_update')(context, vocabData)
                    data = {'name': i, 'vocabulary_id': update_vocab['id']}
                    tk.get_action('tag_create')(context, data)
            for i in smth:
                if i not in myVocab:
                    del_data = {"vocabulary_id": "locations", "id": i}
                    update_vocab = tk.get_action('tag_delete')(context, del_data)
        except tk.ObjectNotFound:
            data = {'name': 'locations'}
            vocab = tk.get_action('vocabulary_create')(context, data)
            for tag in ( u'Khyber Pakhtunkhwa, Pakistan' ,u'Punjab, Pakistan', u'Sindh, Pakistan', u'Balochistan, Pakistan', u'Federal Capital Territory', u'Gilgit Baltistan, Pakistan', u'Azad Kashmir, Pakistan', u'Islamabad, Federal Capital Territory', u'Lahore, Punjab' ,u'Islamabad, Islamabad, Federal Capital Territory', u'Karachi City, Sindh', u'Peshawar, Khyber Pakhtunkhwa'):
                data = {'name': tag, 'vocabulary_id': vocab['id']}
                tk.get_action('tag_create')(context, data)
    
    def locations(self):
        self.create_locations()
        try:
            tag_list = tk.get_action('tag_list')
            locations = tag_list(data_dict={'vocabulary_id': 'locations'})
            return locations
        except tk.ObjectNotFound:
            return None

    def create_data_sources(self):
        user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
        context = {'user': user['name']}
        myVocab = (u'Secondary Research', u'Primary Research', u'tempDataSource')
        try:
            data = {'id': 'data_sources'}
            tag_data = {'vocabulary_id': 'data_sources'}
            
            tk.get_action('vocabulary_show')(context, data)

            smth = tk.get_action('tag_list')(context, tag_data)
            for i in myVocab:
                if i not in smth:
                    vocabData = {"id": "data_sources"}
                    update_vocab = tk.get_action('vocabulary_update')(context, vocabData)
                    data = {'name': i, 'vocabulary_id': update_vocab['id']}
                    tk.get_action('tag_create')(context, data)
            for i in smth:
                if i not in myVocab:
                    del_data = {"vocabulary_id": "data_sources", "id": i}
                    update_vocab = tk.get_action('tag_delete')(context, del_data)

        except tk.ObjectNotFound:

            data = {'name': 'data_sources'}
            vocab = tk.get_action('vocabulary_create')(context, data)
            for tag in (u'Secondary Research', u'Primary Research', u'tempDataSource'):
                data = {'name': tag, 'vocabulary_id': vocab['id']}
                tk.get_action('tag_create')(context, data)
    
    def data_sources(self):
        self.create_data_sources()
        try:
            tag_list = tk.get_action('tag_list')
            data_sources = tag_list(data_dict={'vocabulary_id': 'data_sources'})

            return data_sources
        except tk.ObjectNotFound:
            return None

    def create_data_types(self):
        user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
        context = {'user': user['name']}
        myVocab = (u'geospatial', u'non-geospatial', u'geogeo')
        try:
            data = {'id': 'data_types'}
            tag_data = {'vocabulary_id': 'data_types'}
            
            tk.get_action('vocabulary_show')(context, data)

            smth = tk.get_action('tag_list')(context, tag_data)
            for i in myVocab:
                if i not in smth:
                    vocabData = {"id": "data_types"}
                    update_vocab = tk.get_action('vocabulary_update')(context, vocabData)
                    data = {'name': i, 'vocabulary_id': update_vocab['id']}
                    tk.get_action('tag_create')(context, data)
            for i in smth:
                if i not in myVocab:
                    del_data = {"vocabulary_id": "data_types", "id": i}
                    update_vocab = tk.get_action('tag_delete')(context, del_data)

        except tk.ObjectNotFound:
            data = {'name': 'data_types'}
            vocab = tk.get_action('vocabulary_create')(context, data)
            for tag in (u'geospatial', u'non-geospatial', u'geogeo'):
                data = {'name': tag, 'vocabulary_id': vocab['id']}
                tk.get_action('tag_create')(context, data)
    
    def data_types(self):
        self.create_data_types()
        try:
            tag_list = tk.get_action('tag_list')
            data_types = tag_list(data_dict={'vocabulary_id': 'data_types'})

            return data_types
        except tk.ObjectNotFound:
            return None


    def get_helpers(self):
        return {'categories': self.categories, 'organization_types': self.organization_types, 'data_sources': self.data_sources, 'data_types':self.data_types, 'ODP_Pakistan':self.ODP_Pakistan, 'locations': self.locations}
    
    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True
        
    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
    


    def dataset_facets(self, facets_dict, package_type):
        self._update_facets(facets_dict)
        return facets_dict

    def group_facets(self, facets_dict, group_type, package_type):
        self._update_facets(facets_dict)
        return facets_dict

    def organization_facets(self, facets_dict, organization_type, package_type):
        self._update_facets(facets_dict)
        return facets_dict

    def _update_facets(self, facets_dict):

        del facets_dict['organization']
        del facets_dict['groups']
        # del facets_dict['tags']
        # del facets_dict['res_format']

        facets_dict['data_types'] = p.toolkit._('Data Types')
        facets_dict['categories'] = p.toolkit._('Categories')
        facets_dict['organization_types'] = p.toolkit._('Organization Types')
        facets_dict['data_sources'] = p.toolkit._('data_sources')
        facets_dict['locations'] =p.toolkit._('locations')

        # print("UPDATED FACETS DICT:",facets_dict,'\n')

    def newsaa():
        {'id': '58d70e18-344c-4194-93db-d76065a8ecfe', 'name': 'country_codes',
        'tags': [{'id': '550e73de-2e6d-4b20-9de4-5e1cca5f1c16', 'name': 'de', 'vocabulary_id': '58d70e18-344c-4194-93db-d76065a8ecfe', 'display_name': 'de'},
        {'id': '1a0e94d2-0962-4fb1-9883-773a764d742a', 'name': 'es', 'vocabulary_id': '58d70e18-344c-4194-93db-d76065a8ecfe', 'display_name': 'es'}, {'id': 'f486471a-b2d0-4fac-b021-02226a1b2c21', 'name': 'fr', 'vocabulary_id': '58d70e18-344c-4194-93db-d76065a8ecfe', 'display_name': 'fr'}, {'id': '2dcabfdd-d4cd-4985-a432-df8f20c0362d', 'name': 'ie', 'vocabulary_id': '58d70e18-344c-4194-93db-d76065a8ecfe', 'display_name': 'ie'}, {'id': '64fa271e-76da-4e8e-81c5-29d569d02d4f', 'name': 'uk', 'vocabulary_id': '58d70e18-344c-4194-93db-d76065a8ecfe', 'display_name': 'uk'}]}

        [{'id': '58d70e18-344c-4194-93db-d76065a8ecfe', 'name': 'country_codes', 'tags': [{'id': '1a0e94d2-0962-4fb1-9883-773a764d742a', 'name': 'es', 'vocabulary_id': '58d70e18-344c-4194-93db-d76065a8ecfe', 'display_name': 'es'}, {'id': 'f486471a-b2d0-4fac-b021-02226a1b2c21', 'name': 'fr', 'vocabulary_id': '58d70e18-344c-4194-93db-d76065a8ecfe', 'display_name': 'fr'}, {'id': '2dcabfdd-d4cd-4985-a432-df8f20c0362d', 'name': 'ie', 'vocabulary_id': '58d70e18-344c-4194-93db-d76065a8ecfe', 'display_name': 'ie'}, {'id': '64fa271e-76da-4e8e-81c5-29d569d02d4f', 'name': 'uk', 'vocabulary_id': '58d70e18-344c-4194-93db-d76065a8ecfe', 'display_name': 'uk'}]}, {'id': 'a504f37d-f813-4d35-8209-80545277dcf8', 'name': 'category', 'tags': [{'id': '4f5b2949-d058-4166-aaed-31e8e3f9f708', 'name': 'Demography', 'vocabulary_id': 'a504f37d-f813-4d35-8209-80545277dcf8', 'display_name': 'Demography'}, {'id': '5e98fe5f-e879-44eb-a87a-976086e13388', 'name': 'Economics and Finance', 'vocabulary_id': 'a504f37d-f813-4d35-8209-80545277dcf8', 'display_name': 'Economics and Finance'}, {'id': '41be6081-5005-40d9-9b4a-a86eea8c80b9', 'name': 'Government and Public Sector', 'vocabulary_id': 'a504f37d-f813-4d35-8209-80545277dcf8', 'display_name': 'Government and Public Sector'}, {'id': 'e5ddeffd-32df-45b8-9d1f-af6aeb0bd074', 'name': 'Health', 'vocabulary_id': 'a504f37d-f813-4d35-8209-80545277dcf8', 'display_name': 'Health'}, {'id': '5ffb35a3-b589-4497-aa7c-1f3584664876', 'name': 'Public Safety', 'vocabulary_id': 'a504f37d-f813-4d35-8209-80545277dcf8', 'display_name': 'Public Safety'}]}, {'id': '37948c8b-1e00-4b12-bca1-cb2a1b7c321e', 'name': 'categories', 'tags': [{'id': '816f779b-36f4-430b-bf02-4c33da123b59', 'name': 'Cities and Region', 'vocabulary_id': '37948c8b-1e00-4b12-bca1-cb2a1b7c321e', 'display_name': 'Cities and Region'}, {'id': 'a59081dd-8ed9-4f0b-9c05-18580efeb267', 'name': 'Connectivity', 'vocabulary_id': '37948c8b-1e00-4b12-bca1-cb2a1b7c321e', 'display_name': 'Connectivity'}, {'id': '1c495f35-fa8c-4ba7-874a-d3380e5cde5c', 'name': 'Demography', 'vocabulary_id': '37948c8b-1e00-4b12-bca1-cb2a1b7c321e', 'display_name': 'Demography'}, {'id': 'bd79c0ad-0f9e-4629-a946-768957879fe2', 'name': 'Economics and Finance', 'vocabulary_id': '37948c8b-1e00-4b12-bca1-cb2a1b7c321e', 'display_name': 'Economics and Finance'}, {'id': '0289ffaf-74b1-48ee-9244-16a6701c48f3', 'name': 'Education', 'vocabulary_id': '37948c8b-1e00-4b12-bca1-cb2a1b7c321e', 'display_name': 'Education'}, {'id': '659bc445-e175-4268-9e64-428bc47de3c5', 'name': 'Environment and Energy', 'vocabulary_id': '37948c8b-1e00-4b12-bca1-cb2a1b7c321e', 'display_name': 'Environment and Energy'}, {'id': '41f2e41f-4efd-4e62-9c44-9e2a0b0f0be9', 'name': 'Government and Public Sector', 'vocabulary_id': '37948c8b-1e00-4b12-bca1-cb2a1b7c321e', 'display_name': 'Government and Public Sector'}, {'id': '283e0465-7a5c-46ab-afa2-504d1f446c98', 'name': 'Health', 'vocabulary_id': '37948c8b-1e00-4b12-bca1-cb2a1b7c321e', 'display_name': 'Health'}, {'id': 'bd8724d4-e44c-4855-9090-8e6068c1868a', 'name': 'Housing and Public Sector', 'vocabulary_id': '37948c8b-1e00-4b12-bca1-cb2a1b7c321e', 'display_name': 'Housing and Public Sector'}, {'id': '297ca442-eda1-4026-9a27-8ffd68ed4a1e', 'name': 'Public Safety', 'vocabulary_id': '37948c8b-1e00-4b12-bca1-cb2a1b7c321e', 'display_name': 'Public Safety'}, {'id': '64cde60d-10c4-4ce7-9553-4db712cb1633', 'name': 'new_field', 'vocabulary_id': '37948c8b-1e00-4b12-bca1-cb2a1b7c321e', 'display_name': 'new_field'}, {'id': 'ddb4225a-bdc6-4369-aa24-795725d926c5', 'name': 'saad is kanjar', 'vocabulary_id': '37948c8b-1e00-4b12-bca1-cb2a1b7c321e', 'display_name': 'saad is kanjar'}]}, 
        {'id': '755ee381-3518-48b0-ab33-caf301651cad', 'name': 'organization_types', 'tags': [{'id': '3cfc1ae5-b12c-4405-a3b7-1917d12d6ae4', 'name': 'Educational Institute', 'vocabulary_id': '755ee381-3518-48b0-ab33-caf301651cad', 'display_name': 'Educational Institute'}, {'id': 'bf2ff4bc-57cc-4456-b08c-4cdefa61eaee', 'name': 'Federal Government', 'vocabulary_id': '755ee381-3518-48b0-ab33-caf301651cad', 'display_name': 'Federal Government'}, {'id': 'd606e951-f7fd-49fe-a167-9d50c91f1af2', 'name': 'NGO', 'vocabulary_id': '755ee381-3518-48b0-ab33-caf301651cad', 'display_name': 'NGO'}, {'id': '3855297e-101f-41ca-a3df-08f300139fac', 'name': 'Other', 'vocabulary_id': '755ee381-3518-48b0-ab33-caf301651cad', 'display_name': 'Other'}, {'id': 'f1867398-d592-4709-9f20-2f74caa0a22c', 'name': 'Private Organization', 'vocabulary_id': '755ee381-3518-48b0-ab33-caf301651cad', 'display_name': 'Private Organization'}, {'id': '12e9a48d-c710-424d-83b2-5747f72c628d', 'name': 'Provincial Government', 'vocabulary_id': '755ee381-3518-48b0-ab33-caf301651cad', 'display_name': 'Provincial Government'}]}, {'id': '3811e315-c3c8-496d-a7bc-bc0445675787', 'name': 'data_sources', 'tags': [{'id': '7e98a4e0-72b7-4c0d-9d44-7db35bfcd060', 'name': 'Primary Research', 'vocabulary_id': '3811e315-c3c8-496d-a7bc-bc0445675787', 'display_name': 'Primary Research'}, {'id': '80060a59-0e92-454d-b1d7-890fa0ef331f', 'name': 'Secondary Research', 'vocabulary_id': '3811e315-c3c8-496d-a7bc-bc0445675787', 'display_name': 'Secondary Research'}]}, {'id': 'ce25d651-f24d-4983-8bd7-70e693c589b3', 'name': 'data_types', 'tags': [{'id': 'f8f67ec1-bebb-489d-a6a9-309ff6a8aaa4', 'name': 'Primary Research', 'vocabulary_id': 'ce25d651-f24d-4983-8bd7-70e693c589b3', 'display_name': 'Primary Research'}, {'id': '30c483ff-5100-4602-82d5-49eac72e673e', 'name': 'Secondary Research', 'vocabulary_id': 'ce25d651-f24d-4983-8bd7-70e693c589b3', 'display_name': 'Secondary Research'}]}]




        # u'Khyber Pakhtunkhwa, Pakistan' ,u'Punjab, Pakistan', u'Sindh, Pakistan', u'Balochistan, Pakistan', u'Federal Capital Territory', u'Gilgit Baltistan, Pakistan', u'Azad Kashmir, Pakistan', u'Islamabad, Federal Capital Territory', u'Lahore, Punjab' ,u'Islamabad, Islamabad, Federal Capital Territory', u'Karachi City, Sindh', u'Peshawar, Khyber Pakhtunkhwa'