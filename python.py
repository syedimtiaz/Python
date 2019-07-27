import arcgis
from arcgis.gis import GIS
gis = GIS("https://portalname/arcgis", "username", "password")

#get the list of orphaned items
delete_orphaned_items = gis.content.search(query="owner: ownername AND title:*title*", item_type='Feature *', max_items=100)
delete_orphaned_items

#filter the items 
filtered_items = [item for item in delete_orphaned_items if 'title' in item.title]
print(len(filtered_items))
sorted(filtered_items, key=lambda x:x.title)

#replace dry_run with force. dry_run checks if the item can be safely deleted
for item in filtered_items:
 try:
 item.delete(dry_run=True)
 except TypeError:
 print(f'{item.title} not deleted')
 except RuntimeError:
 print(f'{item.title} not deleted')
