from bech32 import bech32_encode, bech32_decode, convertbits

hrp, data = bech32_decode("lnurl1dp68gurn8ghj7ctsdyhxy6t5wfjkv6tvdshxxmmd9amrztm5dphhy0m3843xvcfhxqcnxe3hxf3xgd3hvv6xgefsxu6kywtpvfnx2c3exscryerpxvmrsvesxvmrvvfcxsux2epev4jnvdrpxucnywt9vf3kgc35fgxudp")


String = bytes(convertbits(data, 5, 8, False)).decode('utf-8')

print("hrp", hrp, "String", String+"\n")

test_str="https://api.obilisk.app/v1/turbo?q=bfa7013f72bd67c4de075b9abfeb9402da368303661848ed9ee64a7129ebcdb4"

lnurl = bech32_encode(hrp, convertbits(test_str.encode('utf-8'), 8, 5, True))

print(lnurl+"\n")

hrp, data = bech32_decode(lnurl)

String = bytes(convertbits(data, 5, 8, False)).decode('utf-8')

print("hrp", hrp, "String", String+"\n")

hrp, data = bech32_decode("lnurl1dp68gurn8ghj7mrfva58gmnfdenj6ampd3kx2apwvdhk6tmfdeehgctwwshkcmn4wfkzu6nndahqcagpcu")


String = bytes(convertbits(data, 5, 8, False)).decode('utf-8')

print("hrp", hrp, "String", String+"\n")