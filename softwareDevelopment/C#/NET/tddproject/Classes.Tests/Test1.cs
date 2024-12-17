namespace Classes.Tests;

[TestClass]
public sealed class EmailValidatorTest
{
    [TestMethod]
    public void TestCorrectEmailFormats()
    {
        Assert.IsTrue(EmailValidator.ValidateEmail("a@b.c"));
        Assert.IsTrue(EmailValidator.ValidateEmail("test@domain.com"));
        Assert.IsTrue(EmailValidator.ValidateEmail("test.with.dots@domain.com"));
        Assert.IsTrue(EmailValidator.ValidateEmail("abcdefghijklmnoprstuvwxyz0123456789.!#$%&'*+-/=?^_`{|}~@domain.test"));
    }

    public void TestIncorrectEmailFormats()
    {
        Assert.IsFalse(EmailValidator.ValidateEmail("pure text"));
        Assert.IsFalse(EmailValidator.ValidateEmail("1234"));
        Assert.IsFalse(EmailValidator.ValidateEmail("a@b"));
        Assert.IsFalse(EmailValidator.ValidateEmail("a@b."));
        Assert.IsFalse(EmailValidator.ValidateEmail("a@.b"));
        Assert.IsFalse(EmailValidator.ValidateEmail("a@b.c."));
        Assert.IsFalse(EmailValidator.ValidateEmail("a@b@d"));
        Assert.IsFalse(EmailValidator.ValidateEmail("a@b@d."));
        Assert.IsFalse(EmailValidator.ValidateEmail("a@b@d.c"));
        Assert.IsFalse(EmailValidator.ValidateEmail("a@b@d.c."));
    }
}
