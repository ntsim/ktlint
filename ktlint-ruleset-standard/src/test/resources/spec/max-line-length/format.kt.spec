fun main() {
    testFunctionWithLongName("fix", "looooooooooooooooooooooooooooooooooooooooooooong", "string")
}

fun testFunctionWithLongName(paramA: String, paramB: String, paramC: String): String {
    return "$paramA + $paramB + $paramC"
}
