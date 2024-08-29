# copy dictionary 

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep si kasep",
    "cuy":" acuy surucuy"
}

friends = teman_teman.copy()
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["cup"]="ucup si keren"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# pop dictionary
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}\n")
print(f"friends = {friends}\n")

# popitem dictionary
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")