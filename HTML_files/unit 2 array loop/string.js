let string="Om Mandhare"

for (let x of string)
{
    document.write(x)
}

for (let x in string)
     {
        document.write(x,"<br>")
    }

len=string.length
document.write("lenght=",len)


upper=string.toUpperCase();
document.write("<br>",upper)


lower=string.toLowerCase();
document.write("<br>",lower)


sliced=string.slice(2,7)
document.write("<br>",sliced,"<br>")


let str="hello "


concatenated =str.concat(string)
document.write(concatenated)