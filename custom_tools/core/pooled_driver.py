import queue
from contextlib import contextmanager
import undetected_chromedriver as uc

from pond import Pond, PooledObjectFactory, PooledObject


class PooledWebDriverFactory(PooledObjectFactory):
    def createInstance(self) -> PooledObject:
        options = uc.ChromeOptions()
        options.binary_location = "/usr/bin/google-chrome"
        options.headless = True
        driver = uc.Chrome(
            options=options,
        )
        return PooledObject(driver)        

    def destroy(self, pooled_object: PooledObject):
        pooled_object.quit()
        del pooled_object

    def reset(self, pooled_object, **kwargs):
        raise NotImplementedError

    def validate(self, pooled_object):
        raise NotImplementedError


web_driver_factory = PooledWebDriverFactory(pooled_maxsize=4, least_one=False)

def build_driver_pool():
    pond = Pond(borrowed_timeout=2,
            time_between_eviction_runs=-1,
            thread_daemon=True,
            eviction_weight=0.8)
    
    pond.register(web_driver_factory)
    return pond;