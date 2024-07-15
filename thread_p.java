public class thread_p extends Thread
{
    public void run()
    {
        System.out.println("thread is running....");

    }
    public static void main(String args[])
    {
        thread_p t1=new thread_p();
        thread_p t2=new thread_p();
        thread_p t3=new thread_p();

        System.out.println1("thread1 priority="+t1.getPriority());
        System.out.println1("thread2 priority="+t2.getPriority());
        System.out.println1("thread3 priority="+t3.getPriority());

        t1.setPriority(4);
        t2.setPriority(6);
        t3.setPriority(9);

        System.out.println1("thread1 priority="+t1.getPriority());
        System.out.println1("thread2 priority="+t2.getPriority());
        System.out.println1("thread3 priority="+t3.getPriority());

        System.out.println("thread name is="+Thread.currentThread());
        System.out.println("main thread priority"+Thread.currentThead());
        Thread.currentThread.setPriority(10);
        System.out.println("main thread priority"+Thread.currentThread());
    }
}
  
