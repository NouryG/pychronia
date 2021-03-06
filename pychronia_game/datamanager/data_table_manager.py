# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from pychronia_game import utilities
from pychronia_game.common import *
from .datamanager_tools import *



class DataTableManager(object):
    """
    Put an instance of this class as an attribute of a datamanager class, 
    to automatically extend it to handle (get/set/delete...)
    a (ZODB) dict of data items.
    """

    TRANSLATABLE_ITEM_NAME = None # must be a lazy-translatable string

    #####INPUT_FIELDS = [] # list of fields allowed in the data dict

    def _load_initial_data(self, **kwargs):
        # NO NEED TO CALL UPPER CLASS !
        raise NotImplementedError("_load_initial_data")

    def _check_database_coherency(self, strict=False, **kwargs):
        # NO NEED TO CALL UPPER CLASS !
        for key, value in self._table.items():
            self._check_item_validity(key, value)


    def _preprocess_new_item(self, key, value):
        """
        Method that completes and normalizes a new item (for example with enforced default values).
        Must return the (possibly modified) (key, value) pair.
        
        Beware of well converting python types to zodb types here if needed.
        """
        raise NotImplementedError("_preprocess_new_item")

    def _check_item_validity(self, key, value, strict=False):
        """
        Method that checks a given item, and raises proper UsageError if it's not OK.
        """
        raise NotImplementedError("_check_item_validity")

    def _sorting_key(self, item_pair):
        """
        Method that returns the key used to sort items, when a sorted list is asked for.
        *item_pair* is a (key, value) pair as returned by dict.items()
        """
        raise NotImplementedError("_sorting_key")

    def _get_table_container(self, root):
        """
        Method that browses the root container to return the concerned data "table" as a dict.
        """
        raise NotImplementedError("_get_table_container")

    def _item_can_be_edited(self, key, value):
        """
        Returns True iff item can be safely modified and removed from list.
        """
        raise NotImplementedError("_item_can_be_edited")


    def __init__(self, datamanager):
        self._inner_datamanager = datamanager # do not change name -> used by decorators!
        assert self.TRANSLATABLE_ITEM_NAME

    @property
    def _table(self):
        return self._get_table_container(self._inner_datamanager.data)

    @classmethod
    def _check_item_is_in_table(cls, table, key):
        if key not in table:
            raise AbnormalUsageError(_("Couldn't find %(type)s item with key %(key)s") % SDICT(type=cls.TRANSLATABLE_ITEM_NAME, key=key))

    @classmethod
    def _check_item_is_not_in_table(cls, table, key):
        if key in table:
            raise AbnormalUsageError(_("Items of type %(type)s with key %(key)s already exists") % SDICT(type=cls.TRANSLATABLE_ITEM_NAME, key=key))

    @readonly_method
    def get_all_data(self, as_sorted_list=False, mutability=None):
        """
        returns STANDARD python objects, no ZODB ones.
        
        If mutability is not None, then its value is enforced for selected items.
        """
        items_gen = self._table.items()
        if mutability is not None:
            items_gen = ((k, v) for (k, v) in items_gen if bool(self._item_can_be_edited(k, v)) == bool(mutability))
        if not as_sorted_list:
            data = dict(items_gen)
        else:
            data = list(items_gen)
            data.sort(key=self._sorting_key)

        data = utilities.convert_object_tree(data, type_mapping=utilities.zodb_to_python_types)
        if __debug__: 
            utilities.check_object_tree(data, allowed_types=utilities.allowed_python_types, path=[])
            import json
            json.dumps(data)  # compatibility test
        return data

    @readonly_method
    def __len__(self):
        return len(self._table)

    @readonly_method
    def __contains__(self, key):
        return (key in self._table)

    @readonly_method
    def __getitem__(self, key):
        table = self._table
        self._check_item_is_in_table(table, key)
        return table[key]

    @transaction_watcher
    def __setitem__(self, key, value):
        table = self._table
        if key in table and not self._item_can_be_edited(key, table[key]):
            raise AbnormalUsageError(_("Can't modify %(type)s item with key %(key)s") % SDICT(type=self.TRANSLATABLE_ITEM_NAME, key=key))
        ###value = {k: v for (k, v) in value.items() if k in self.INPUT_FIELDS} # we filter out useless values
        key, value = self._preprocess_new_item(key, value)
        self._check_item_validity(key, value)
        table[key] = value

    @transaction_watcher
    def __delitem__(self, key):
        table = self._table
        self._check_item_is_in_table(table, key)
        if not self._item_can_be_edited(key, table[key]):
            raise AbnormalUsageError(_("Can't delete %(type)s item with key %(key)s") % SDICT(type=self.TRANSLATABLE_ITEM_NAME, key=key))
        del table[key]

    @readonly_method
    def copy(self):
        """Shallow copy"""
        return dict(**self._table) # thus no WRITE on dict

    # transaction watching here would make no sense
    def __getattr__(self, name):
        return getattr(self._table, name) # for methods like keys()... don't use copy() as it's MODIFYING object



class LazyInstantiationDescriptor(object):
    """
    Used to place a special attribute in datamanager modules, 
    proxying to a new instance of DataTableManager on attribute access.
    """
    def __init__(self, target_klass):
        self.target_klass = target_klass

    def __get__(self, obj, objtype):
        return self.target_klass(datamanager=obj)










