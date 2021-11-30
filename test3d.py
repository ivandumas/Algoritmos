from py3dbp import Packer, Bin, Item

packer = Packer()

packer.add_bin(Bin('small', 300,300,200,5))
packer.add_bin(Bin('big', 500,600,400,8))

packer.add_item(Item('Producto 1',45,60,70,0.5))
packer.add_item(Item('Producto 2',30,50,30,0.7))
packer.add_item(Item('Producto 3',20,70,70,1))
packer.add_item(Item('Producto 4',45,60,70,1.2))
packer.add_item(Item('Producto 5',170,80,70,1.2))
packer.add_item(Item('Producto 6',300,200,70,1.2))

packer.pack(bigger_first=True)

for b in packer.bins:
    print(":::::::::::", b.string())

    print("FITTED ITEMS:")
    for item in b.items:
        print("====> ", item.string())

    print("UNFITTED ITEMS:")
    for item in b.unfitted_items:
        print("====> ", item.string())

    print("***************************************************")
    print("***************************************************")