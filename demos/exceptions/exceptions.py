import myclasses
import traceback

print("hello world!")

try:
    instancia = myclasses.MyClassA()
    instancia.method1()

except ZeroDivisionError:
    print("A division by zero again! :C")

except Exception:
    tb = traceback.format_exc()
    print(tb)

print("Goodbye")