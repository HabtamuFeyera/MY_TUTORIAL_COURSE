def get_net_price(price, discount):
    return price * (1-discount)


net_price = get_net_price(50, 0.5)
print(net_price)